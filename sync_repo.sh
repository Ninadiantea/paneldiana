#!/bin/bash

# Sync Repository Script for MyXL Bot
# Usage: ./sync_repo.sh

echo "🔄 Syncing Repository with Remote"
echo "=================================="

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository!"
    echo "💡 Please run this script from the project directory"
    exit 1
fi

# Check current branch
CURRENT_BRANCH=$(git branch --show-current)
echo "📋 Current branch: $CURRENT_BRANCH"

# Check remote status
echo "🌐 Checking remote status..."
git fetch origin

# Check if local is behind remote
LOCAL_COMMIT=$(git rev-parse HEAD)
REMOTE_COMMIT=$(git rev-parse origin/$CURRENT_BRANCH)

if [ "$LOCAL_COMMIT" != "$REMOTE_COMMIT" ]; then
    echo "⚠️  Local repository is behind remote!"
    echo "📥 Pulling latest changes..."
    
    # Check for conflicts
    if [ -n "$(git status --porcelain)" ]; then
        echo "⚠️  You have uncommitted changes!"
        echo "📝 Options:"
        echo "1. Stash changes and pull"
        echo "2. Commit changes first"
        echo "3. Cancel"
        
        read -p "🤔 Choose option (1/2/3): " -n 1 -r
        echo
        
        case $REPLY in
            1)
                echo "📦 Stashing changes..."
                git stash
                STASHED=true
                ;;
            2)
                echo "💾 Please commit your changes first:"
                echo "   git add . && git commit -m 'Your message'"
                exit 1
                ;;
            3)
                echo "❌ Sync cancelled"
                exit 0
                ;;
            *)
                echo "❌ Invalid option"
                exit 1
                ;;
        esac
    fi
    
    # Pull changes
    git pull origin $CURRENT_BRANCH
    
    if [ $? -eq 0 ]; then
        echo "✅ Successfully pulled updates!"
        
        # Restore stashed changes if any
        if [ "$STASHED" = true ]; then
            echo "📦 Restoring stashed changes..."
            git stash pop
        fi
        
        # Update dependencies if needed
        if git diff --name-only HEAD~1 HEAD | grep -q "requirements.txt"; then
            echo "📦 Requirements.txt changed, updating dependencies..."
            source venv/bin/activate
            pip install -r requirements.txt
        fi
        
    else
        echo "❌ Failed to pull updates!"
        echo "💡 There might be conflicts. Please resolve them manually."
        exit 1
    fi
else
    echo "✅ Local repository is up to date!"
fi

# Check if local is ahead of remote
LOCAL_COMMIT=$(git rev-parse HEAD)
REMOTE_COMMIT=$(git rev-parse origin/$CURRENT_BRANCH)

if [ "$LOCAL_COMMIT" != "$REMOTE_COMMIT" ]; then
    echo "📤 Local repository is ahead of remote!"
    echo "💡 You have commits that need to be pushed."
    
    read -p "🤔 Do you want to push changes? (y/n): " -n 1 -r
    echo
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "📤 Pushing changes..."
        git push origin $CURRENT_BRANCH
        
        if [ $? -eq 0 ]; then
            echo "✅ Successfully pushed changes!"
        else
            echo "❌ Failed to push changes!"
            echo "💡 Check your internet connection and repository permissions"
        fi
    fi
fi

echo ""
echo "📊 Repository Status:"
git status --short

echo ""
echo "📋 Recent commits:"
git log --oneline -5

echo ""
echo "🎉 Repository sync completed!"