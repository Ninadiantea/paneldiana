# Git Repository Management 📚

## Quick Start 🚀

### Pull Latest Updates
```bash
./pull_updates.sh
```

### Push Your Changes
```bash
./push_changes.sh
```

### Sync Repository (Recommended)
```bash
./sync_repo.sh
```

## Script Details 📋

### 1. `pull_updates.sh` - Pull Latest Changes
**Fitur:**
- ✅ Check uncommitted changes
- ✅ Auto stash jika ada perubahan
- ✅ Fetch dan pull dari remote
- ✅ Auto update dependencies jika requirements.txt berubah
- ✅ Restore stashed changes

**Usage:**
```bash
./pull_updates.sh
```

### 2. `push_changes.sh` - Push Your Changes
**Fitur:**
- ✅ Check perubahan yang belum di-commit
- ✅ Input commit message (atau auto-generate)
- ✅ Add, commit, dan push otomatis
- ✅ Show recent commits

**Usage:**
```bash
./push_changes.sh
```

### 3. `sync_repo.sh` - Complete Sync
**Fitur:**
- ✅ Check status local vs remote
- ✅ Auto pull jika behind
- ✅ Auto push jika ahead
- ✅ Handle conflicts
- ✅ Update dependencies

**Usage:**
```bash
./sync_repo.sh
```

## Manual Git Commands 🔧

### Check Status
```bash
git status
```

### Add Changes
```bash
git add .
git add filename.py
```

### Commit Changes
```bash
git commit -m "Your commit message"
```

### Push to Remote
```bash
git push origin main
git push origin your-branch
```

### Pull from Remote
```bash
git pull origin main
git pull origin your-branch
```

### Check Branches
```bash
git branch -a
git checkout branch-name
```

### View History
```bash
git log --oneline
git log --oneline -10
```

## Common Scenarios 🔄

### Scenario 1: Ada Update Baru
```bash
# Option 1: Auto sync
./sync_repo.sh

# Option 2: Manual
git pull origin main
```

### Scenario 2: Ada Perubahan Lokal
```bash
# Option 1: Auto push
./push_changes.sh

# Option 2: Manual
git add .
git commit -m "Your changes"
git push origin main
```

### Scenario 3: Conflict Resolution
```bash
# 1. Check conflicts
git status

# 2. Edit conflicted files
nano conflicted_file.py

# 3. Add resolved files
git add .

# 4. Commit resolution
git commit -m "Resolve conflicts"

# 5. Push
git push origin main
```

### Scenario 4: Stash Changes
```bash
# Stash changes
git stash

# Pull updates
git pull origin main

# Restore changes
git stash pop
```

## Best Practices 💡

### 1. Regular Sync
```bash
# Sync setiap hari
./sync_repo.sh
```

### 2. Meaningful Commits
```bash
# Good commit messages
git commit -m "Fix message length error in bot"
git commit -m "Add new package feature"
git commit -m "Update documentation"

# Bad commit messages
git commit -m "fix"
git commit -m "update"
```

### 3. Check Before Push
```bash
# Always check status first
git status
git diff

# Then push
./push_changes.sh
```

### 4. Backup Important Changes
```bash
# Create backup branch
git checkout -b backup/feature-name

# Push backup
git push origin backup/feature-name
```

## Troubleshooting 🔧

### Error: "Permission denied"
```bash
# Check remote URL
git remote -v

# Set up SSH key or use HTTPS
git remote set-url origin https://github.com/username/repo.git
```

### Error: "Merge conflict"
```bash
# 1. Check conflicts
git status

# 2. Edit files with conflicts
# Look for <<<<<<< HEAD markers

# 3. Resolve and add
git add .

# 4. Commit
git commit -m "Resolve merge conflicts"
```

### Error: "Branch is behind"
```bash
# Pull latest changes
./pull_updates.sh

# Or manual
git pull origin main
```

### Error: "Cannot lock ref"
```bash
# Clean up git locks
rm -rf .git/refs/heads/.lock
rm -rf .git/index.lock
```

## Repository Structure 📁

```
myxl-cli/
├── .git/                    # Git repository
├── telegram_bot.py          # Main bot file
├── config.py               # Bot configuration
├── requirements.txt        # Dependencies
├── pull_updates.sh         # Pull script
├── push_changes.sh         # Push script
├── sync_repo.sh           # Sync script
└── README.md              # Documentation
```

## Auto-Update Workflow 🔄

### Daily Workflow
```bash
# 1. Start work
./sync_repo.sh

# 2. Make changes
# ... edit files ...

# 3. Save changes
./push_changes.sh

# 4. End work
./sync_repo.sh
```

### Weekly Maintenance
```bash
# 1. Check for updates
./pull_updates.sh

# 2. Update dependencies
pip install -r requirements.txt

# 3. Test bot
./start_bot.sh

# 4. Commit any fixes
./push_changes.sh
```

---

**💡 Tip**: Gunakan `./sync_repo.sh` sebagai command utama untuk sync repository. Script ini akan handle semua scenario secara otomatis!