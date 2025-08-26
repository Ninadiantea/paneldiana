#!/usr/bin/env python3
"""
Test bot dengan logging detail untuk debug
"""

import logging
import sys
from telegram_bot import main

# Setup detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot_debug.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Enable debug logging for specific modules
logging.getLogger('telegram_bot').setLevel(logging.DEBUG)
logging.getLogger('paket_xut').setLevel(logging.DEBUG)
logging.getLogger('api_request').setLevel(logging.DEBUG)

def main_with_logging():
    """Run bot with detailed logging"""
    print("🔍 Starting bot with detailed logging...")
    print("📝 Logs will be saved to bot_debug.log")
    print("💡 Press Ctrl+C to stop")
    print("-" * 50)
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        logging.error(f"Bot crashed: {e}", exc_info=True)

if __name__ == "__main__":
    main_with_logging()