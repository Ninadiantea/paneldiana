#!/bin/bash

# Install MyXL Bot as Systemd Service
# Usage: ./install_service.sh

echo "🔧 Installing MyXL Bot as Systemd Service"
echo "=========================================="

# Get current user
CURRENT_USER=$(whoami)
echo "👤 Current user: $CURRENT_USER"

# Get current directory
CURRENT_DIR=$(pwd)
echo "📁 Current directory: $CURRENT_DIR"

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "❌ Don't run as root!"
    exit 1
fi

# Check if config is set
if grep -q "YOUR_BOT_TOKEN_HERE" config.py; then
    echo "❌ Bot token not configured!"
    echo "💡 Please edit config.py and set your bot token first"
    exit 1
fi

# Create service file
echo "📝 Creating service file..."
cat > myxl-bot.service << EOF
[Unit]
Description=MyXL Telegram Bot
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
WorkingDirectory=$CURRENT_DIR
Environment=PATH=$CURRENT_DIR/venv/bin
ExecStart=$CURRENT_DIR/venv/bin/python $CURRENT_DIR/bot_service.py
Restart=always
RestartSec=30
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

# Copy service file to systemd
echo "📦 Installing service..."
sudo cp myxl-bot.service /etc/systemd/system/

# Reload systemd
echo "🔄 Reloading systemd..."
sudo systemctl daemon-reload

# Enable service
echo "✅ Enabling service..."
sudo systemctl enable myxl-bot.service

echo ""
echo "✅ Service installed successfully!"
echo ""
echo "📋 Service commands:"
echo "  Start:   sudo systemctl start myxl-bot"
echo "  Stop:    sudo systemctl stop myxl-bot"
echo "  Status:  sudo systemctl status myxl-bot"
echo "  Logs:    sudo journalctl -u myxl-bot -f"
echo ""
echo "🚀 Starting service..."
sudo systemctl start myxl-bot.service

echo ""
echo "📊 Service status:"
sudo systemctl status myxl-bot.service --no-pager -l

echo ""
echo "📝 To view logs:"
echo "  sudo journalctl -u myxl-bot -f"