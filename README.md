# MyXL CLI & Telegram Bot 🤖

Aplikasi untuk mengelola akun MyXL dengan interface CLI dan Telegram Bot!

## Fitur Utama ✨

### CLI Interface
- 🔐 Login dengan OTP
- 💰 Cek saldo dan masa aktif
- 📦 Beli paket XUT
- 🔄 Ganti akun

### Telegram Bot
- 🤖 Interface chat yang mudah
- 📱 Menu dengan tombol inline
- 🔐 Login dengan OTP via chat
- 💰 Cek saldo real-time
- 📦 Beli paket dengan satu klik
- 🔄 Ganti akun dengan mudah

## Quick Start 🚀

### CLI Mode
```bash
# Install dependencies
source venv/bin/activate
pip install -r requirements.txt

# Run CLI
python3 main.py
```

### Telegram Bot Mode
```bash
# 1. Setup bot token di config.py
# 2. Install dependencies
source venv/bin/activate
pip install -r requirements.txt

# 3. Run bot
python3 run_bot.py

# Atau gunakan script
./start_bot.sh
```

## File Structure 📁

```
myxl-cli/
├── main.py                 # CLI interface
├── telegram_bot.py         # Telegram bot
├── config.py              # Bot configuration
├── api_request.py         # MyXL API functions
├── crypto_helper.py       # Encryption helpers
├── paket_xut.py          # XUT package functions
├── ui.py                 # CLI UI functions
├── util.py               # Utility functions
├── requirements.txt       # Dependencies
├── run_bot.py            # Bot runner
├── bot_service.py        # Bot service (auto-restart)
├── start_bot.sh          # Start script
├── stop_bot.sh           # Stop script
├── status_bot.sh         # Status script
├── setup_bot.md          # Bot setup guide
├── README_TELEGRAM_BOT.md # Bot documentation
└── README.md             # This file
```

## Bot Management 🛠️

### Start Bot
```bash
./start_bot.sh
```

### Stop Bot
```bash
./stop_bot.sh
```

### Check Status
```bash
./status_bot.sh
```

### Manual Run
```bash
python3 run_bot.py
```

## Setup Bot Telegram 📱

1. **Buat bot** di [@BotFather](https://t.me/BotFather)
2. **Edit config.py** dan masukkan token bot
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Jalankan bot**: `./start_bot.sh`

Lihat [setup_bot.md](setup_bot.md) untuk panduan lengkap.

## Bot Commands 🤖

- `/start` - Mulai bot dan tampilkan menu utama
- Login dengan OTP via chat
- Cek saldo dengan tombol
- Beli paket dengan satu klik

## Keamanan 🔒

- Token MyXL tidak disimpan permanen
- Setiap user session terpisah
- Data sensitif hanya di memory
- Auto-restart pada error

## Troubleshooting 🔧

### CLI Issues
- Pastikan dependencies terinstall
- Cek format nomor telepon (628xxx)
- Pastikan OTP 6 digit

### Bot Issues
- Cek token bot di config.py
- Pastikan bot sudah dijalankan
- Lihat log di bot_service.log

### Dependencies
```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Dependencies 📦

- `requests` - HTTP requests
- `pycryptodome` - Encryption
- `brotli` - Compression
- `python-telegram-bot` - Telegram Bot API

## Contributing 🤝

1. Fork repository
2. Buat feature branch
3. Commit changes
4. Push ke branch
5. Buat Pull Request

## License 📄

Project ini menggunakan lisensi yang sama dengan myxl-cli original.

---

**Note**: Aplikasi ini menggunakan API MyXL yang tidak resmi. Gunakan dengan bijak dan sesuai dengan Terms of Service MyXL.

## Support 💬

Jika ada masalah atau pertanyaan:
- Buat issue di repository
- Cek troubleshooting guide
- Lihat dokumentasi bot di [README_TELEGRAM_BOT.md](README_TELEGRAM_BOT.md)
