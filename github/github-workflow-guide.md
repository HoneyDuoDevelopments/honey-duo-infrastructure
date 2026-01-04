# GitHub Workflow Guide - Honey Duo Infrastructure

**For:** Sam (learning Git/GitHub)  
**Purpose:** Clear, simple instructions for managing code across Pi and Ubuntu  
**Last Updated:** January 4, 2026

---

## 🎯 The One Rule You Need to Remember

```
┌────────────────────────────────────────────────────────┐
│  BEFORE working → git pull                             │
│  AFTER working  → git add, commit, push                │
└────────────────────────────────────────────────────────┘
```

That's it. Everything else is just details.

---

## 📚 Understanding Git in Plain English

### What is Git?

Git is like "Track Changes" in Word, but for code. It remembers every change you make.

### What is GitHub?

GitHub is like Dropbox for code - it's where your code lives "in the cloud." Both your Pi and Ubuntu can access it.

### How They Work Together

```
┌──────────────┐                    ┌──────────────┐
│ Raspberry Pi │                    │    Ubuntu    │
│              │                    │              │
│  Your Code   │                    │  Your Code   │
│      ↕       │                    │      ↕       │
│  Local Git   │                    │  Local Git   │
└──────┬───────┘                    └──────┬───────┘
       │                                   │
       │     push (upload your changes)    │
       │  ─────────────────────────────►   │
       │                                   │
       │  ┌────────────────────────────┐   │
       └─►│         GitHub             │◄──┘
          │   (shared storage in cloud)│
          └────────────────────────────┘
       ┌──│                            │──┐
       │  │                            │  │
       │     pull (download changes)      │
       ▼  ◄─────────────────────────────  ▼
```

**Key Concept:** Git does NOT automatically sync. You must tell it to push (upload) and pull (download).

---

## 🔄 Daily Workflow

### Scenario 1: Starting Work on Pi

```bash
# Step 1: Go to your project folder
cd ~/honey-duo-infrastructure

# Step 2: Get any changes from GitHub (ALWAYS do this first!)
git pull origin main

# Step 3: Do your work (edit files, create files, etc.)
# ... make your changes ...

# Step 4: When done, check what you changed
git status

# Step 5: Add your changes (the dot means "all changes")
git add .

# Step 6: Commit with a message explaining what you did
git commit -m "Added new feature XYZ"

# Step 7: Upload to GitHub
git push origin main
```

### Scenario 2: Switching to Ubuntu

```bash
# Step 1: Go to your project folder
cd ~/honey-duo-infrastructure

# Step 2: Get the changes you just pushed from Pi
git pull origin main

# Now your Ubuntu has all the Pi changes!
```

### Scenario 3: You Forgot to Pull First (Conflict!)

If you edited on Ubuntu without pulling first, and Pi had changes:

```bash
# This might happen:
git pull origin main
# ERROR: "Your local changes would be overwritten"

# Solution - save your changes temporarily:
git stash

# Now pull:
git pull origin main

# Get your changes back:
git stash pop

# If there's a conflict, Git will mark it. Edit the file to fix.
# Then:
git add .
git commit -m "Merged my changes"
git push origin main
```

---

## 📋 Command Reference Card

### Commands You'll Use Daily

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `git pull origin main` | Download latest from GitHub | **Before** starting work |
| `git status` | Show what files changed | Check before committing |
| `git add .` | Stage all changes | After making changes |
| `git commit -m "message"` | Save changes with description | After git add |
| `git push origin main` | Upload to GitHub | After committing |

### Commands You'll Use Sometimes

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `git log --oneline -5` | Show last 5 commits | See what changed recently |
| `git diff` | Show exactly what changed | Before committing |
| `git stash` | Temporarily save changes | When you need to pull but have unsaved work |
| `git stash pop` | Restore stashed changes | After pulling |

### Commands for Problems

| Command | What It Does | When to Use |
|---------|--------------|-------------|
| `git checkout -- filename` | Undo changes to one file | You messed up a file |
| `git reset --hard HEAD` | Undo ALL changes | Nuclear option - discards everything |
| `git fetch origin` | Check for updates without downloading | See if GitHub has changes |

---

## 🆕 Adding a New Repository

When you create a new project (like a new trading bot or app):

### Step 1: Create on GitHub Website

1. Go to https://github.com/HoneyDuoDevelopments
2. Click green "New" button
3. Name: `your-project-name` (lowercase, hyphens)
4. Description: Brief explanation
5. ✅ Private (unless you want it public)
6. ✅ Add README
7. Click "Create repository"

### Step 2: Clone to Your Computer

```bash
# On the system where this project will live (Pi or Ubuntu)
cd ~
git clone git@github.com:HoneyDuoDevelopments/your-project-name.git

# Verify it worked
cd your-project-name
ls -la
```

### Step 3: Update Documentation

```bash
# Go to infrastructure repo
cd ~/honey-duo-infrastructure

# Edit the repositories list
nano github/REPOSITORIES.md
# Add your new repo to the list

# If it's a Pi project, create integration folder:
mkdir -p pi/your-project-name
nano pi/your-project-name/README.md

# If it's an Ubuntu project:
mkdir -p ubuntu/your-project-name
nano ubuntu/your-project-name/README.md

# Commit the documentation
git add .
git commit -m "Add documentation for your-project-name"
git push origin main
```

### Step 4: Start Building

```bash
# Go to your new project
cd ~/your-project-name

# Make changes, then commit frequently:
git add .
git commit -m "Initial project structure"
git push origin main
```

---

## 🔗 Integrating New Systems into Infrastructure

When you build something new, it needs to connect to your monitoring/infrastructure:

### Integration Checklist

For every new service, you need:

1. **Documentation** in infrastructure repo
   - `pi/` or `ubuntu/` subfolder
   - README explaining the service
   
2. **Monitoring** (after Phase 0 Component 3)
   - Add to Uptime Kuma
   - Configure alerts
   
3. **Metrics** (after Phase 0 Component 4)
   - Add to Prometheus scrape config
   - Create Grafana dashboard
   
4. **Logging** (after Phase 0 Component 5)
   - Configure Promtail to ship logs
   
5. **Secrets** (after Phase 0 Component 2)
   - Store passwords in Vaultwarden
   - Update code to use environment variables

### Example: Adding a New Python App

```bash
# 1. Create the repo (follow steps above)

# 2. In infrastructure repo, create integration docs:
cd ~/honey-duo-infrastructure
mkdir -p ubuntu/my-new-app

cat > ubuntu/my-new-app/README.md << 'EOF'
# My New App

**Location:** ~/my-new-app
**Repo:** https://github.com/HoneyDuoDevelopments/my-new-app
**Port:** 8080

## Service Management
```bash
sudo systemctl status my-new-app
sudo systemctl restart my-new-app
```

## Monitoring Integration
- Uptime Kuma: HTTP check on port 8080
- Prometheus: /metrics endpoint
- Logs: /var/log/my-new-app.log
EOF

# 3. Commit infrastructure docs
git add .
git commit -m "Add my-new-app integration documentation"
git push origin main

# 4. Create the actual app in its own repo
cd ~/my-new-app
# ... build your app ...
git add .
git commit -m "Initial app code"
git push origin main
```

---

## 🏠 Repository Locations Quick Reference

### On Raspberry Pi (192.168.0.193)

| Repo | Path | Purpose |
|------|------|---------|
| honey-duo-infrastructure | `~/honey-duo-infrastructure` | All configs & docs |
| honey-duo-gaming | `/home/honeyduopi/Desktop/HoneyDuoGaming` | N64 emulation |

### On Ubuntu (192.168.0.245)

| Repo | Path | Purpose |
|------|------|---------|
| honey-duo-infrastructure | `~/honey-duo-infrastructure` | All configs & docs |
| design-duo | `~/design-duo` | AI image gen (future) |
| ira-trading-duo | `~/ira-trading-duo` | Trading bots (future) |

---

## 🚨 Common Mistakes & Fixes

### Mistake 1: "I forgot to pull before working"

**Symptom:** `git push` fails with "rejected" error

**Fix:**
```bash
git pull origin main
# If conflict, edit the file to resolve
git add .
git commit -m "Merged changes"
git push origin main
```

### Mistake 2: "I committed a secret/password"

**Symptom:** You see a password in your commit

**Fix (if not pushed yet):**
```bash
git reset --soft HEAD~1  # Undo last commit, keep changes
# Edit the file to remove secret
git add .
git commit -m "Fixed message"
```

**Fix (if already pushed):**
- Change the password immediately
- Use git filter-branch or BFG Repo-Cleaner (advanced)
- Or accept it's in history and just change the password

### Mistake 3: "I'm on the wrong branch"

**Check:**
```bash
git branch  # Shows current branch with asterisk
```

**Fix:**
```bash
git checkout main  # Switch to main branch
```

### Mistake 4: "I don't know what changed"

**Check:**
```bash
git status  # What files changed
git diff    # What exactly changed in those files
```

---

## 💡 Tips for Success

### Commit Often
```bash
# Good: Multiple small commits
git commit -m "Added login page"
git commit -m "Added user validation"
git commit -m "Fixed login bug"

# Bad: One giant commit
git commit -m "Added everything"
```

### Write Good Commit Messages
```bash
# Good messages:
"Add Vaultwarden docker-compose config"
"Fix Pi-hole DNS timeout issue"
"Update monitoring dashboard with GPU temps"

# Bad messages:
"stuff"
"fixed it"
"asdfasdf"
```

### Pull Before You Push
Make it a habit:
```bash
git pull origin main  # Get latest
git push origin main  # Then push yours
```

### When in Doubt, Check Status
```bash
git status
```
This never hurts and always helps.

---

## 🆘 Getting Help

### If You're Stuck

1. Run `git status` - it usually tells you what to do next
2. Check `git log --oneline -5` to see recent history
3. Ask Claude (share the exact error message)
4. Google the error (Git errors are very common)

### Useful Links

- [GitHub Docs](https://docs.github.com)
- [Git Cheat Sheet (PDF)](https://training.github.com/downloads/github-git-cheat-sheet.pdf)
- [Interactive Git Tutorial](https://learngitbranching.js.org)

---

## 📅 Quick Daily Checklist

```
Morning (starting work):
□ cd ~/honey-duo-infrastructure
□ git pull origin main
□ Start working

Finishing (done for now):
□ git status (check what changed)
□ git add .
□ git commit -m "What I did"
□ git push origin main

Switching systems:
□ Push on current system
□ Pull on new system before working
```

---

**Remember:** Git is a tool to help you, not hurt you. If something goes wrong, there's almost always a way to fix it. The worst case is you re-clone the repo from GitHub and lose uncommitted changes - which is why you commit often!