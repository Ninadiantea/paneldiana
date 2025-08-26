#!/usr/bin/env python3
"""
Simple script to run MyXL Telegram Bot
"""

import sys
import os
from telegram_bot import main

def check_config():
    """Check if bot token is configured"""
    try:
        from config import BOT_TOKEN
        if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
            print("❌ Error: Bot token belum dikonfigurasi!")
            print("📝 Silakan edit file config.py dan ganti BOT_TOKEN dengan token bot Anda")
            print("🤖 Dapatkan token dari @BotFather di Telegram")
            return False
        return True
    except ImportError:
        print("❌ Error: File config.py tidak ditemukan!")
        return False

def check_dependencies():
    """Check if all dependencies are installed"""
    try:
        import telegram
        import requests
        import brotli
        import zlib
        import base64
        from Crypto.Cipher import AES
        print("✅ Semua dependencies terinstall")
        return True
    except ImportError as e:
        print(f"❌ Error: Dependency tidak terinstall - {e}")
        print("💡 Jalankan: pip install -r requirements.txt")
        return False

def main_wrapper():
    """Main wrapper with error handling"""
    print("🤖 MyXL Telegram Bot")
    print("=" * 30)
    
    # Check config
    if not check_config():
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("🚀 Memulai bot...")
    print("💡 Tekan Ctrl+C untuk menghentikan bot")
    print("-" * 30)
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Bot dihentikan oleh user")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main_wrapper()