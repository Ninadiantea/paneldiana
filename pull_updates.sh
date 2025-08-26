#!/bin/bash

# Pull Updates Script for MyXL Bot
# Usage: ./pull_updates.sh

echo "🔄 Pulling Latest Updates"
echo "=========================="

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository!"
    echo "💡 Please run this script from the project directory"
    exit 1
fi

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "📋 Current branch: $CURRENT_BRANCH"

# Check if there are uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Warning: You have uncommitted changes!"
    echo "📝 Changes:"
    git status --short
    
    read -p "🤔 Do you want to stash changes before pulling? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📦 Stashing changes..."
        git stash
        STASHED=true
    else
        echo "❌ Please commit or stash your changes first"
        exit 1
    fi
fi

# Fetch latest changes
echo "📥 Fetching latest changes..."
git fetch origin

# Check if there are updates
LOCAL_COMMIT=$(git rev-parse HEAD)
REMOTE_COMMIT=$(git rev-parse origin/$CURRENT_BRANCH)

if [ "$LOCAL_COMMIT" = "$REMOTE_COMMIT" ]; then
    echo "✅ Already up to date!"
else
    echo "🔄 Pulling updates..."
    git pull origin $CURRENT_BRANCH
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully pulled updates!"
        
        # Show recent commits
        echo "📋 Recent commits:"
        git log --oneline -5
        
        # Restore stashed changes if any
        if [ "$STASHED" = true ]; then
            echo "📦 Restoring stashed changes..."
            git stash pop
        fi
        
        # Update dependencies if requirements.txt changed
        if git diff --name-only HEAD~1 HEAD | grep -q "requirements.txt"; then
            echo "📦 Requirements.txt changed, updating dependencies..."
            source venv/bin/activate
            pip install -r requirements.txt
        fi
        
        echo ""
        echo "🎉 Repository updated successfully!"
        echo "💡 You may need to restart the bot:"
        echo "   ./stop_bot.sh && ./start_bot.sh"
        
    else
        echo "❌ Failed to pull updates!"
        echo "💡 Check for conflicts or network issues"
        exit 1
    fi
fi

echo ""
echo "📊 Repository Status:"
git status --short