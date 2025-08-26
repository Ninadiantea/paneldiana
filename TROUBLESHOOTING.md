# Troubleshooting MyXL Bot 🤖

## Masalah: Paket XUT Tidak Muncul

### Gejala
- Bot berjalan normal
- Login berhasil
- Saat klik "📦 Paket XUT" tidak ada respon atau muncul error

### Penyebab Umum

#### 1. Token Expired
**Gejala**: Bot tidak merespon saat klik Paket XUT
**Solusi**:
```bash
# Login ulang dengan bot
# Atau restart bot
./stop_bot.sh
./start_bot.sh
```

#### 2. API MyXL Bermasalah
**Gejala**: Error "Failed to get family data"
**Solusi**:
- Cek koneksi internet
- Coba lagi beberapa menit kemudian
- API MyXL mungkin sedang maintenance

#### 3. Data Structure Berubah
**Gejala**: Error parsing data
**Solusi**:
- Update kode untuk handle struktur data baru
- Cek log untuk detail error

## Masalah: "Message is too long" Error

### Gejala
- Error saat input OTP atau menampilkan paket
- Bot crash dengan error "Message is too long"

### Penyebab
- Telegram memiliki batasan maksimal 4096 karakter per pesan
- Pesan yang dikirim terlalu panjang

### Solusi
- ✅ **Sudah diperbaiki** - Bot sekarang otomatis memotong pesan panjang
- ✅ **Split messages** - Pesan panjang akan dibagi menjadi beberapa bagian
- ✅ **Truncate long text** - Teks yang terlalu panjang akan dipotong

### Debug
```bash
# Test message length handling
python3 test_message_length.py
```

### Gejala
- Bot berjalan normal
- Login berhasil
- Saat klik "📦 Paket XUT" tidak ada respon atau muncul error

### Penyebab Umum

#### 1. Token Expired
**Gejala**: Bot tidak merespon saat klik Paket XUT
**Solusi**:
```bash
# Login ulang dengan bot
# Atau restart bot
./stop_bot.sh
./start_bot.sh
```

#### 2. API MyXL Bermasalah
**Gejala**: Error "Failed to get family data"
**Solusi**:
- Cek koneksi internet
- Coba lagi beberapa menit kemudian
- API MyXL mungkin sedang maintenance

#### 3. Data Structure Berubah
**Gejala**: Error parsing data
**Solusi**:
- Update kode untuk handle struktur data baru
- Cek log untuk detail error

### Debug Steps

#### Step 1: Cek Log Bot
```bash
# Jalankan bot dengan logging detail
python3 test_bot_with_logging.py

# Atau cek log file
tail -f bot_debug.log
```

#### Step 2: Test Package Loading
```bash
# Setelah login, test package loading
python3 test_packages.py
```

#### Step 3: Cek Token Status
```bash
# Cek apakah token masih valid
python3 debug_bot.py
```

### Debug Commands

#### 1. Test Bot dengan Logging Detail
```bash
python3 test_bot_with_logging.py
```

#### 2. Test Package Loading Manual
```bash
python3 test_packages.py
```

#### 3. Debug Bot State
```bash
python3 debug_bot.py
```

#### 4. Cek Log Files
```bash
# Bot service log
tail -f bot_service.log

# Debug log
tail -f bot_debug.log
```

### Common Error Messages

#### "Token tidak valid"
```bash
# Login ulang dengan bot
# Atau restart bot
./stop_bot.sh
./start_bot.sh
```

#### "Tidak ada paket tersedia"
- Cek apakah nomor XL masih aktif
- Cek apakah ada paket XUT tersedia
- Coba refresh token

#### "Failed to get family data"
- Cek koneksi internet
- API MyXL mungkin bermasalah
- Coba lagi nanti

#### "Error saat memuat paket"
- Cek log untuk detail error
- Mungkin ada perubahan di API MyXL

### Prevention Tips

#### 1. Regular Token Refresh
- Bot akan auto-refresh token
- Jika gagal, login ulang

#### 2. Monitor Logs
```bash
# Cek status bot
./status_bot.sh

# Monitor logs
tail -f bot_service.log
```

#### 3. Keep Bot Updated
- Update dependencies regularly
- Monitor API changes

### Advanced Debugging

#### 1. Enable Verbose Logging
Edit `config.py`:
```python
LOG_LEVEL = "DEBUG"
```

#### 2. Test API Directly
```python
# Test API call
from api_request import get_family
from paket_xut import get_package_xut

# Load tokens
with open("tokens.json", "r") as f:
    tokens = json.load(f)

# Test get_family
data = get_family(tokens, "08a3b1e6-8e78-4e45-a540-b40f06871cfe")
print(data)

# Test get_package_xut
packages = get_package_xut(tokens)
print(packages)
```

#### 3. Check Network
```bash
# Test connectivity to MyXL API
curl -I https://api.myxl.xlaxiata.co.id
```

### Getting Help

#### 1. Collect Debug Info
```bash
# Run debug script
python3 debug_bot.py > debug_output.txt

# Collect logs
cp bot_service.log debug_logs.txt
cp bot_debug.log debug_logs.txt

# Check status
./status_bot.sh > status.txt
```

#### 2. Share Information
- Debug output
- Error messages
- Log files
- Steps to reproduce

### Quick Fixes

#### Bot Tidak Merespon
```bash
./stop_bot.sh
./start_bot.sh
```

#### Login Gagal
- Cek format nomor (628xxx)
- Cek OTP (6 digit)
- Coba login ulang

#### Package Tidak Muncul
```bash
# Restart bot
./stop_bot.sh
./start_bot.sh

# Login ulang
# Coba klik Paket XUT
```

---

**Note**: Jika masalah masih berlanjut, cek log files dan share error details untuk bantuan lebih lanjut.