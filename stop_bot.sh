#!/bin/bash

# MyXL Telegram Bot Stop Script
# Usage: ./stop_bot.sh

echo "🛑 Stopping MyXL Telegram Bot..."

# Find and kill bot processes
BOT_PIDS=$(ps aux | grep -E "(bot_service.py|telegram_bot.py)" | grep -v grep | awk '{print $2}')

if [ -z "$BOT_PIDS" ]; then
    echo "✅ No bot processes found"
else
    echo "🔍 Found bot processes: $BOT_PIDS"
    for pid in $BOT_PIDS; do
        echo "🛑 Killing process $pid..."
        kill $pid
    done
    echo "✅ Bot stopped"
fi

# Clean up any remaining processes
sleep 2
REMAINING_PIDS=$(ps aux | grep -E "(bot_service.py|telegram_bot.py)" | grep -v grep | awk '{print $2}')
if [ ! -z "$REMAINING_PIDS" ]; then
    echo "🔨 Force killing remaining processes..."
    for pid in $REMAINING_PIDS; do
        kill -9 $pid
    done
fi

echo "👋 Bot service stopped"