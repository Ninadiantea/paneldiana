#!/bin/bash

# MyXL Telegram Bot Deployment Script
# Usage: ./deploy.sh

echo "🚀 MyXL Telegram Bot Deployment"
echo "================================"

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "❌ Don't run as root!"
    exit 1
fi

# Update system
echo "📦 Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install required packages
echo "📦 Installing required packages..."
sudo apt install -y python3 python3-pip python3-venv git curl

# Create virtual environment
echo "🐍 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Make scripts executable
echo "🔧 Making scripts executable..."
chmod +x start_bot.sh stop_bot.sh status_bot.sh

# Check if config needs to be set
if grep -q "YOUR_BOT_TOKEN_HERE" config.py; then
    echo ""
    echo "⚠️  IMPORTANT: Bot token not configured!"
    echo "📝 Please edit config.py and set your bot token"
    echo "🤖 Get token from @BotFather on Telegram"
    echo ""
    echo "Example:"
    echo "BOT_TOKEN = \"123456789:ABCdefGHIjklMNOpqrsTUVwxyz\""
    echo ""
fi

echo "✅ Deployment completed!"
echo ""
echo "📋 Next steps:"
echo "1. Edit config.py and set your bot token"
echo "2. Run: ./start_bot.sh"
echo "3. Check status: ./status_bot.sh"
echo ""
echo "📚 Documentation:"
echo "- Setup guide: setup_bot.md"
echo "- Bot docs: README_TELEGRAM_BOT.md"
echo ""