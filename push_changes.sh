#!/bin/bash

# Push Changes Script for MyXL Bot
# Usage: ./push_changes.sh

echo "📤 Pushing Changes to Repository"
echo "================================"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository!"
    echo "💡 Please run this script from the project directory"
    exit 1
fi

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "📋 Current branch: $CURRENT_BRANCH"

# Check if there are changes to commit
if [ -z "$(git status --porcelain)" ]; then
    echo "✅ No changes to commit!"
    echo "💡 All changes are already committed"
    exit 0
fi

# Show current changes
echo "📝 Current changes:"
git status --short

# Ask for commit message
echo ""
read -p "💬 Enter commit message (or press Enter for default): " COMMIT_MSG

if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="Update MyXL Bot - $(date '+%Y-%m-%d %H:%M:%S')"
fi

# Add all changes
echo "📦 Adding changes..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "$COMMIT_MSG"

if [ $? -eq 0 ]; then
    echo "✅ Changes committed successfully!"
    
    # Push to remote
    echo "📤 Pushing to remote repository..."
    git push origin $CURRENT_BRANCH
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully pushed to remote!"
        echo "🎉 Repository updated!"
        
        # Show recent commits
        echo ""
        echo "📋 Recent commits:"
        git log --oneline -3
        
    else
        echo "❌ Failed to push to remote!"
        echo "💡 Check your internet connection and repository permissions"
        exit 1
    fi
else
    echo "❌ Failed to commit changes!"
    exit 1
fi

echo ""
echo "📊 Repository Status:"
git status --short