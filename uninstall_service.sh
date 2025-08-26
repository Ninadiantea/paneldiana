#!/bin/bash

# Uninstall MyXL Bot Systemd Service
# Usage: ./uninstall_service.sh

echo "🗑️  Uninstalling MyXL Bot Systemd Service"
echo "=========================================="

# Stop service
echo "🛑 Stopping service..."
sudo systemctl stop myxl-bot.service

# Disable service
echo "❌ Disabling service..."
sudo systemctl disable myxl-bot.service

# Remove service file
echo "🗑️  Removing service file..."
sudo rm -f /etc/systemd/system/myxl-bot.service

# Reload systemd
echo "🔄 Reloading systemd..."
sudo systemctl daemon-reload

# Reset failed units
echo "🔄 Resetting failed units..."
sudo systemctl reset-failed

echo ""
echo "✅ Service uninstalled successfully!"
echo ""
echo "📋 Remaining files:"
echo "  - Bot files: $(pwd)"
echo "  - Virtual environment: $(pwd)/venv"
echo "  - Logs: $(pwd)/bot_service.log"
echo ""
echo "💡 To run bot manually:"
echo "  ./start_bot.sh"