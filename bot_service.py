#!/usr/bin/env python3
"""
MyXL Telegram Bot Service
Untuk menjalankan bot sebagai service dengan auto-restart
"""

import time
import sys
import logging
from datetime import datetime
from telegram_bot import main

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot_service.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_bot_service():
    """Run bot with auto-restart on error"""
    restart_count = 0
    max_restarts = 10
    
    while restart_count < max_restarts:
        try:
            logger.info(f"🤖 Starting MyXL Bot (attempt {restart_count + 1}/{max_restarts})")
            logger.info(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Run the bot
            main()
            
        except KeyboardInterrupt:
            logger.info("👋 Bot stopped by user")
            break
            
        except Exception as e:
            restart_count += 1
            logger.error(f"❌ Bot crashed: {e}")
            logger.info(f"🔄 Restarting in 30 seconds... (attempt {restart_count}/{max_restarts})")
            
            if restart_count >= max_restarts:
                logger.error("🚨 Max restart attempts reached. Stopping service.")
                break
                
            time.sleep(30)  # Wait 30 seconds before restart
    
    logger.info("👋 Bot service stopped")

if __name__ == "__main__":
    print("🤖 MyXL Telegram Bot Service")
    print("=" * 40)
    print("💡 Press Ctrl+C to stop")
    print("🔄 Auto-restart on crash enabled")
    print("-" * 40)
    
    run_bot_service()