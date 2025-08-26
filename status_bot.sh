#!/bin/bash

# MyXL Telegram Bot Status Script
# Usage: ./status_bot.sh

echo "📊 MyXL Telegram Bot Status"
echo "=========================="

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "✅ Virtual environment: Found"
else
    echo "❌ Virtual environment: Not found"
fi

# Check if config is set
if grep -q "YOUR_BOT_TOKEN_HERE" config.py; then
    echo "❌ Bot token: Not configured"
else
    echo "✅ Bot token: Configured"
fi

# Check if dependencies are installed
if python3 -c "import telegram" 2>/dev/null; then
    echo "✅ Dependencies: Installed"
else
    echo "❌ Dependencies: Not installed"
fi

# Check if bot is running
BOT_PIDS=$(ps aux | grep -E "(bot_service.py|telegram_bot.py)" | grep -v grep | awk '{print $2}')

if [ -z "$BOT_PIDS" ]; then
    echo "❌ Bot status: Not running"
else
    echo "✅ Bot status: Running (PID: $BOT_PIDS)"
    
    # Show uptime
    for pid in $BOT_PIDS; do
        UPTIME=$(ps -o etime= -p $pid 2>/dev/null)
        if [ ! -z "$UPTIME" ]; then
            echo "⏰ Uptime: $UPTIME"
        fi
    done
fi

# Check log file
if [ -f "bot_service.log" ]; then
    LOG_SIZE=$(du -h bot_service.log | cut -f1)
    echo "📝 Log file: Found (Size: $LOG_SIZE)"
else
    echo "📝 Log file: Not found"
fi

echo "=========================="