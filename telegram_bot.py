import os
import json
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from api_request import get_otp, submit_otp, save_tokens, get_package, purchase_package, get_profile, get_balance, get_new_token
from paket_xut import get_package_xut

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

from config import BOT_TOKEN

# User states untuk tracking conversation
user_states = {}
user_data = {}

def truncate_message(text: str, max_length: int = 4000) -> str:
    """Truncate message to avoid Telegram's message length limit"""
    if len(text) <= max_length:
        return text
    
    # Try to truncate at a reasonable point
    truncated = text[:max_length-3] + "..."
    return truncated

def split_long_message(text: str, max_length: int = 4000) -> list:
    """Split long message into multiple parts"""
    if len(text) <= max_length:
        return [text]
    
    parts = []
    while text:
        if len(text) <= max_length:
            parts.append(text)
            break
        
        # Find a good break point
        break_point = text.rfind('\n', 0, max_length)
        if break_point == -1:
            break_point = text.rfind(' ', 0, max_length)
        if break_point == -1:
            break_point = max_length
        
        parts.append(text[:break_point])
        text = text[break_point:].lstrip()
    
    return parts

def load_token():
    """Load token dari file"""
    if os.path.exists("tokens.json"):
        with open("tokens.json", "r", encoding="utf8") as f:
            tokens = json.load(f)
        
        refresh_token = tokens.get("refresh_token")
        tokens = get_new_token(refresh_token)
        
        id_token = tokens.get("id_token")
        access_token = tokens.get("access_token")
        
        profile = get_profile(access_token, id_token)
        if not profile:
            return None
        
        phone_number = profile.get("profile").get("msisdn")
        
        balance = get_balance(id_token)
        balance_remaining = balance.get("remaining")
        balance_expired_at = balance.get("expired_at")
        
        return {
            "tokens": tokens,
            "is_logged_in": True,
            "phone_number": phone_number,
            "balance": balance_remaining,
            "balance_expired_at": balance_expired_at,
        }
    
    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk command /start"""
    user_id = update.effective_user.id
    
    # Load user data
    user_data[user_id] = load_token() or {
        "is_logged_in": False,
        "phone_number": None,
        "balance": None,
        "balance_expired_at": None,
        "tokens": None,
    }
    
    await show_main_menu(update, context)

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Tampilkan menu utama"""
    user_id = update.effective_user.id
    user_info = user_data.get(user_id, {})
    
    if not user_info.get("is_logged_in"):
        message = "🤖 *MyXL Bot*\n\n"
        message += "Selamat datang di MyXL Bot!\n"
        message += "Anda belum login. Silakan login terlebih dahulu."
        
        keyboard = [
            [InlineKeyboardButton("🔐 Login", callback_data="login")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        if update.callback_query:
            await update.callback_query.edit_message_text(
                text=message, 
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        else:
            await update.message.reply_text(
                text=message, 
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
    else:
        phone_number = user_info["phone_number"]
        remaining_balance = user_info["balance"]
        expired_at = user_info["balance_expired_at"]
        expired_at_dt = datetime.fromtimestamp(expired_at).strftime("%Y-%m-%d %H:%M:%S")
        
        message = "🤖 *MyXL Bot*\n\n"
        message += f"📱 *Nomor:* `{phone_number}`\n"
        message += f"💰 *Pulsa:* Rp `{remaining_balance:,}`\n"
        message += f"⏰ *Masa aktif:* `{expired_at_dt}`\n\n"
        message += "Pilih menu di bawah ini:"
        
        keyboard = [
            [InlineKeyboardButton("🔄 Ganti Akun", callback_data="login")],
            [InlineKeyboardButton("📦 Paket XUT", callback_data="packages")],
            [InlineKeyboardButton("💰 Cek Saldo", callback_data="balance")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        if update.callback_query:
            await update.callback_query.edit_message_text(
                text=message, 
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
        else:
            await update.message.reply_text(
                text=message, 
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )

async def handle_login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk login"""
    user_id = update.effective_user.id
    user_states[user_id] = "waiting_phone"
    
    message = "🔐 *Login MyXL*\n\n"
    message += "Masukkan nomor XL Prabayar Anda\n"
    message += "Format: `6281234567890`\n\n"
    message += "Contoh: `6281234567890`"
    
    keyboard = [[InlineKeyboardButton("🔙 Kembali", callback_data="main_menu")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.edit_message_text(
        text=message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def handle_phone_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk input nomor telepon"""
    user_id = update.effective_user.id
    phone_number = update.message.text.strip()
    
    if user_states.get(user_id) != "waiting_phone":
        return
    
    if not phone_number.startswith("628") or len(phone_number) < 10 or len(phone_number) > 14:
        await update.message.reply_text(
            "❌ Nomor tidak valid!\n\n"
            "Pastikan nomor diawali dengan '628' dan memiliki panjang yang benar.\n"
            "Contoh: `6281234567890`",
            parse_mode='Markdown'
        )
        return
    
    try:
        await update.message.reply_text("📤 Mengirim OTP...")
        subscriber_id = get_otp(phone_number)
        
        if not subscriber_id:
            await update.message.reply_text("❌ Gagal mengirim OTP. Silakan coba lagi.")
            user_states[user_id] = None
            return
        
        user_states[user_id] = "waiting_otp"
        context.user_data["phone_number"] = phone_number
        context.user_data["subscriber_id"] = subscriber_id
        
        # Split message to avoid "Message is too long" error
        message1 = "✅ OTP berhasil dikirim!"
        message2 = f"📱 Nomor: `{phone_number}`\n\nMasukkan kode OTP yang telah dikirim:"
        
        keyboard = [[InlineKeyboardButton("🔙 Kembali", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Send first message
        await update.message.reply_text(
            text=message1,
            parse_mode='Markdown'
        )
        
        # Send second message with keyboard
        await update.message.reply_text(
            text=message2,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    except Exception as e:
        error_msg = str(e)
        if "Message is too long" in error_msg:
            await update.message.reply_text("❌ Pesan terlalu panjang. Silakan coba lagi.")
        else:
            await update.message.reply_text(f"❌ Error: {error_msg[:200]}")
        user_states[user_id] = None

async def handle_otp_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk input OTP"""
    user_id = update.effective_user.id
    otp = update.message.text.strip()
    
    if user_states.get(user_id) != "waiting_otp":
        return
    
    if not otp.isdigit() or len(otp) != 6:
        await update.message.reply_text(
            "❌ OTP tidak valid!\n\n"
            "Pastikan OTP terdiri dari 6 digit angka."
        )
        return
    
    phone_number = context.user_data.get("phone_number")
    
    try:
        await update.message.reply_text("🔐 Memverifikasi OTP...")
        tokens = submit_otp(phone_number, otp)
        
        if not tokens:
            await update.message.reply_text("❌ Gagal login. Periksa OTP dan coba lagi.")
            user_states[user_id] = None
            return
        
        save_tokens(tokens)
        
        # Update user data
        user_data[user_id] = load_token()
        
        await update.message.reply_text("✅ Login berhasil!")
        user_states[user_id] = None
        
        # Show main menu
        await show_main_menu(update, context)
        
    except Exception as e:
        error_msg = str(e)
        if "Message is too long" in error_msg:
            await update.message.reply_text("❌ Pesan terlalu panjang. Silakan coba lagi.")
        else:
            await update.message.reply_text(f"❌ Error: {error_msg[:200]}")
        user_states[user_id] = None

async def handle_packages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk menampilkan paket"""
    user_id = update.effective_user.id
    user_info = user_data.get(user_id, {})
    
    if not user_info.get("is_logged_in"):
        await update.callback_query.answer("❌ Anda harus login terlebih dahulu!")
        return
    
    try:
        await update.callback_query.answer("📦 Memuat paket...")
        
        # Debug: Log user info
        logger.info(f"User {user_id} requesting packages")
        logger.info(f"User tokens: {user_info.get('tokens', {}).keys()}")
        
        # Check if tokens are valid and refresh if needed
        if not user_info.get("tokens") or not user_info["tokens"].get("id_token"):
            message = "❌ Token tidak valid. Silakan login ulang."
            keyboard = [[InlineKeyboardButton("🔙 Kembali", callback_data="main_menu")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.callback_query.edit_message_text(text=message, reply_markup=reply_markup)
            return
        
        # Try to refresh token if we have refresh_token
        try:
            if user_info["tokens"].get("refresh_token"):
                logger.info("Refreshing token...")
                new_tokens = get_new_token(user_info["tokens"]["refresh_token"])
                if new_tokens:
                    user_info["tokens"] = new_tokens
                    user_data[user_id] = user_info
                    logger.info("Token refreshed successfully")
        except Exception as e:
            logger.warning(f"Failed to refresh token: {str(e)}")
        
        packages = get_package_xut(user_info["tokens"])
        
        # Debug: Log packages result
        logger.info(f"Packages result: {packages}")
        
        if not packages:
            message = "❌ Tidak ada paket tersedia saat ini.\n\n"
            message += "Mungkin:\n"
            message += "• Token sudah expired\n"
            message += "• Tidak ada paket XUT tersedia\n"
            message += "• Ada masalah dengan API MyXL"
            keyboard = [[InlineKeyboardButton("🔙 Kembali", callback_data="main_menu")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.callback_query.edit_message_text(text=message, reply_markup=reply_markup)
            return
        
        # Create shorter message to avoid "Message is too long" error
        message = "📦 *Paket XUT Tersedia*\n\n"
        message += f"Tersedia {len(packages)} paket:\n\n"
        
        # Add package list (limited to avoid long message)
        for i, package in enumerate(packages[:5]):  # Limit to 5 packages
            price_formatted = f"{package['price']:,}"
            message += f"{i+1}. {package['name']}\n"
            message += f"   💰 Rp {price_formatted}\n\n"
        
        if len(packages) > 5:
            message += f"...dan {len(packages) - 5} paket lainnya\n\n"
        
        keyboard = []
        for package in packages:
            price_formatted = f"{package['price']:,}"
            # Truncate button text if too long
            button_text = f"{package['name'][:30]} - Rp {price_formatted}"
            if len(button_text) > 64:  # Telegram button limit
                button_text = f"{package['name'][:20]} - Rp {price_formatted}"
            keyboard.append([InlineKeyboardButton(button_text, callback_data=f"buy_{package['code']}")])
        
        keyboard.append([InlineKeyboardButton("🔙 Kembali", callback_data="main_menu")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(
            text=message,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    except Exception as e:
        logger.error(f"Error in handle_packages: {str(e)}")
        
        # Handle "Message is too long" error specifically
        if "Message is too long" in str(e):
            message = "❌ Pesan terlalu panjang untuk ditampilkan.\n\n"
            message += "Silakan coba lagi atau hubungi admin."
        else:
            message = f"❌ Error saat memuat paket:\n{str(e)[:200]}"
        
        keyboard = [[InlineKeyboardButton("🔙 Kembali", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.callback_query.edit_message_text(text=message, reply_markup=reply_markup)

async def handle_buy_package(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk membeli paket"""
    user_id = update.effective_user.id
    user_info = user_data.get(user_id, {})
    
    if not user_info.get("is_logged_in"):
        await update.callback_query.answer("❌ Anda harus login terlebih dahulu!")
        return
    
    package_code = update.callback_query.data.replace("buy_", "")
    
    try:
        await update.callback_query.answer("🛒 Memproses pembelian...")
        
        # Get package details first
        packages = get_package_xut(user_info["tokens"])
        package = next((p for p in packages if p["code"] == package_code), None)
        
        if not package:
            await update.callback_query.answer("❌ Paket tidak ditemukan!")
            return
        
        # Purchase package
        result = purchase_package(user_info["tokens"], package_code)
        
        if result and result.get("success"):
            message = f"✅ *Pembelian Berhasil!*\n\n"
            message += f"📦 Paket: {package['name'][:50]}\n"
            message += f"💰 Harga: Rp {package['price']:,}\n"
            message += f"📱 Nomor: {user_info['phone_number']}"
        else:
            message = f"❌ *Pembelian Gagal!*\n\n"
            message += f"📦 Paket: {package['name'][:50]}\n"
            message += f"💰 Harga: Rp {package['price']:,}\n"
            if result:
                error_msg = result.get('message', 'Unknown error')
                message += f"Error: {error_msg[:100]}"
        
        # Truncate message if too long
        message = truncate_message(message)
        
        keyboard = [[InlineKeyboardButton("🔙 Kembali", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(
            text=message,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    except Exception as e:
        await update.callback_query.answer(f"❌ Error: {str(e)}")

async def handle_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk cek saldo"""
    user_id = update.effective_user.id
    user_info = user_data.get(user_id, {})
    
    if not user_info.get("is_logged_in"):
        await update.callback_query.answer("❌ Anda harus login terlebih dahulu!")
        return
    
    # Refresh balance
    try:
        tokens = get_new_token(user_info["tokens"]["refresh_token"])
        balance = get_balance(tokens["id_token"])
        
        remaining_balance = balance.get("remaining")
        expired_at = balance.get("expired_at")
        expired_at_dt = datetime.fromtimestamp(expired_at).strftime("%Y-%m-%d %H:%M:%S")
        
        message = "💰 *Informasi Saldo*\n\n"
        message += f"📱 Nomor: `{user_info['phone_number']}`\n"
        message += f"💰 Pulsa: Rp `{remaining_balance:,}`\n"
        message += f"⏰ Masa aktif: `{expired_at_dt}`"
        
        keyboard = [[InlineKeyboardButton("🔙 Kembali", callback_data="main_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.callback_query.edit_message_text(
            text=message,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
        
    except Exception as e:
        await update.callback_query.answer(f"❌ Error: {str(e)}")

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk callback queries"""
    query = update.callback_query
    data = query.data
    
    if data == "main_menu":
        await show_main_menu(update, context)
    elif data == "login":
        await handle_login(update, context)
    elif data == "packages":
        await handle_packages(update, context)
    elif data == "balance":
        await handle_balance(update, context)
    elif data.startswith("buy_"):
        await handle_buy_package(update, context)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler untuk pesan teks"""
    user_id = update.effective_user.id
    
    if user_states.get(user_id) == "waiting_phone":
        await handle_phone_input(update, context)
    elif user_states.get(user_id) == "waiting_otp":
        await handle_otp_input(update, context)
    else:
        await update.message.reply_text(
            "🤖 Gunakan /start untuk memulai bot atau pilih menu yang tersedia."
        )

def main():
    """Main function"""
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start bot
    print("🤖 MyXL Bot started...")
    application.run_polling()

if __name__ == "__main__":
    main()