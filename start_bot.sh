#!/bin/bash

# MyXL Telegram Bot Startup Script
# Usage: ./start_bot.sh

echo "🤖 Starting MyXL Telegram Bot..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "💡 Please run: python3 -m venv venv"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if dependencies are installed
if ! python3 -c "import telegram" 2>/dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Check if config is set
if grep -q "YOUR_BOT_TOKEN_HERE" config.py; then
    echo "❌ Bot token not configured!"
    echo "💡 Please edit config.py and set your bot token"
    exit 1
fi

# Start the bot
echo "🚀 Starting bot..."
python3 bot_service.py