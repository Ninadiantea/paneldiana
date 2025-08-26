# MyXL Telegram Bot 🤖

Bot Telegram untuk mengelola akun MyXL Anda dengan mudah melalui chat!

## Fitur ✨

- 🔐 **Login dengan OTP** - Login ke akun MyXL menggunakan nomor telepon dan OTP
- 💰 **Cek Saldo** - Lihat saldo pulsa dan masa aktif akun
- 📦 **Paket XUT** - Lihat dan beli paket Xtra Combo Unli Turbo
- 🔄 **Ganti Akun** - Login dengan akun MyXL yang berbeda
- 📱 **Interface Mudah** - Menu dengan tombol inline yang user-friendly

## Cara Setup 🚀

### 1. Buat Bot Telegram

1. Buka Telegram dan chat dengan [@BotFather](https://t.me/BotFather)
2. Kirim `/newbot`
3. Ikuti instruksi untuk membuat bot baru
4. Salin token bot yang diberikan

### 2. Setup Environment

1. Install dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

2. Edit file `config.py`:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Ganti dengan token bot Anda
```

### 3. Jalankan Bot

```bash
source venv/bin/activate
python3 telegram_bot.py
```

## Cara Penggunaan 📖

### 1. Start Bot
- Chat dengan bot Anda dan kirim `/start`
- Bot akan menampilkan menu utama

### 2. Login
- Klik tombol "🔐 Login"
- Masukkan nomor XL Prabayar (format: 6281234567890)
- Masukkan kode OTP yang dikirim ke nomor Anda

### 3. Cek Saldo
- Setelah login, klik "💰 Cek Saldo"
- Bot akan menampilkan informasi saldo dan masa aktif

### 4. Beli Paket
- Klik "📦 Paket XUT"
- Pilih paket yang ingin dibeli
- Konfirmasi pembelian

## Struktur File 📁

```
myxl-cli/
├── telegram_bot.py          # File utama bot Telegram
├── config.py               # Konfigurasi bot
├── api_request.py          # API MyXL (existing)
├── crypto_helper.py        # Helper encryption (existing)
├── paket_xut.py           # Paket XUT (existing)
├── requirements.txt        # Dependencies
└── README_TELEGRAM_BOT.md  # Dokumentasi ini
```

## Keamanan 🔒

- Bot hanya menyimpan token sementara di memory
- Data sensitif tidak disimpan secara permanen
- Setiap user memiliki session terpisah

## Troubleshooting 🔧

### Bot tidak merespon
- Pastikan token bot benar
- Cek apakah bot sudah dijalankan
- Pastikan semua dependencies terinstall

### Login gagal
- Pastikan nomor telepon benar (format: 628xxx)
- Cek apakah OTP sudah benar
- Pastikan nomor adalah XL Prabayar

### Error "Module not found"
- Jalankan: `pip install -r requirements.txt`
- Pastikan virtual environment aktif

## Kontribusi 🤝

Silakan berkontribusi dengan:
- Melaporkan bug
- Menambahkan fitur baru
- Memperbaiki dokumentasi

## Lisensi 📄

Project ini menggunakan lisensi yang sama dengan myxl-cli original.

---

**Note**: Bot ini menggunakan API MyXL yang tidak resmi. Gunakan dengan bijak dan sesuai dengan Terms of Service MyXL.