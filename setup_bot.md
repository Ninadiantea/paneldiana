# Setup MyXL Telegram Bot - Langkah demi Langkah 🚀

## Langkah 1: Buat Bot Telegram

1. **Buka Telegram** dan cari [@BotFather](https://t.me/BotFather)
2. **Kirim pesan** `/newbot`
3. **Masukkan nama bot** (contoh: "MyXL Manager")
4. **Masukkan username bot** (contoh: "myxl_manager_bot") - harus berakhir dengan 'bot'
5. **Salin token bot** yang diberikan (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

## Langkah 2: Konfigurasi Bot

1. **Edit file `config.py`**:
```python
BOT_TOKEN = "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"  # Ganti dengan token Anda
```

2. **Simpan file**

## Langkah 3: Install Dependencies

```bash
# Aktifkan virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Langkah 4: Jalankan Bot

```bash
# Jalankan bot
python3 run_bot.py
```

## Langkah 5: Test Bot

1. **Buka Telegram** dan cari username bot Anda
2. **Kirim `/start`**
3. **Test fitur login** dengan nomor XL Anda

## Troubleshooting 🔧

### Bot tidak merespon
- ✅ Pastikan token bot benar
- ✅ Cek apakah bot sudah dijalankan
- ✅ Pastikan semua dependencies terinstall

### Error "Module not found"
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Bot token invalid
- ✅ Dapatkan token baru dari @BotFather
- ✅ Pastikan format token benar
- ✅ Restart bot setelah ganti token

## Fitur Bot 🤖

- 🔐 **Login MyXL** dengan OTP
- 💰 **Cek saldo** dan masa aktif
- 📦 **Beli paket XUT**
- 🔄 **Ganti akun**

## Keamanan 🔒

- Bot hanya menyimpan data sementara
- Token MyXL tidak disimpan permanen
- Setiap user session terpisah

---

**Note**: Pastikan nomor telepon adalah XL Prabayar dan format OTP benar (6 digit).