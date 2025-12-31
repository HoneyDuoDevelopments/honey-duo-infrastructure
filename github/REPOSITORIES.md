# Honey Duo - GitHub Repositories

Master reference for all GitHub repositories in the Honey Duo ecosystem.

**Purpose:** This document ensures Claude has access to all code for assistance and code review.

---

## Active Repositories

### 1. honey-duo-infrastructure
**URL:** https://github.com/HoneyDuoDevelopments/honey-duo-infrastructure  
**Purpose:** Infrastructure configurations, monitoring, documentation  
**Systems:** Both Pi and Ubuntu  
**Location Pi:** `/home/honeyduopi/honey-duo-infrastructure`  
**Location Ubuntu:** `/home/honey-duo/honey-duo-infrastructure`  
**Status:** ✅ Active - Phase 0 in progress

**What's here:**
- All monitoring configurations (Prometheus, Grafana, Loki)
- Service integration documentation
- Network topology and architecture docs
- Operational runbooks and procedures
- This GitHub reference directory

**Development workflow:**
- Work on either system
- Commit and push frequently
- Pull on other system before starting work
- See: `docs/github-workflow.md`

---

### 2. honey-duo-gaming
**URL:** https://github.com/HoneyDuoDevelopments/honey-duo-gaming  
**Purpose:** N64 emulation web control interface  
**System:** Raspberry Pi  
**Location:** `/home/honeyduopi/Desktop/HoneyDuoGaming`  
**Status:** ✅ Active - Running in production

**What's here:**
- Flask web application for RetroArch control
- Remote game launching interface
- Save state management
- Integration with Cloudflare tunnel (pi.honey-duo.com)

**Integration:**
- Monitored via Uptime Kuma
- Logs shipped to Loki
- Systemd service: `honeyduo-gaming.service`
- See: `pi/gaming/README.md` in infrastructure repo

---

### 3. design-duo
**URL:** https://github.com/HoneyDuoDevelopments/design-duo  
**Purpose:** AI image generation for Sticker Duo  
**System:** Ubuntu RTX 3090  
**Location:** `/home/honey-duo/design-duo`  
**Status:** 🚧 Placeholder - Phase 1

**What will be here:**
- ComfyUI integration
- API wrapper for programmatic access
- Model configurations (SDXL, LoRAs)
- Batch processing queue
- Integration with Sticker Duo platform

**Integration:**
- Will use RTX 3090 GPU (24GB VRAM)
- Monitored via Uptime Kuma, Prometheus, Grafana
- Logs to Loki
- External access via Cloudflare tunnel
- See: `ubuntu/design-duo/README.md` in infrastructure repo

**Development starts:** After Phase 0 complete

---

### 4. ira-trading-duo
**URL:** https://github.com/HoneyDuoDevelopments/ira-trading-duo  
**Purpose:** Automated trading infrastructure  
**System:** Ubuntu  
**Location:** `/home/honey-duo/ira-trading-duo`  
**Status:** 🚧 Placeholder - Future phase

**What will be here:**
- Trading bot framework
- Broker API integrations
- Strategy implementations
- Database schema and migrations
- Comprehensive test suite
- Audit logging system

**Integration:**
- Critical monitoring (30s health checks)
- Immediate Discord alerts on failure
- Comprehensive audit logging to Loki
- All secrets in Vaultwarden
- Emergency access via VPN and web terminals
- See: `ubuntu/ira-trading-duo/README.md` in infrastructure repo

**Development starts:** After Phase 0 and initial trading strategy design

---

## Future Repositories

### sticker-duo (Planned)
**Purpose:** E-commerce platform for custom stickers  
**System:** TBD (likely Ubuntu or cloud)  
**Status:** Concept phase

**Will integrate with:**
- DesignDuo for AI-generated designs
- Vaultwarden for credentials
- Monitoring infrastructure

---

## Repository Locations Summary

**Raspberry Pi:**
```
/home/honeyduopi/
├── honey-duo-infrastructure/     # Infrastructure configs
└── Desktop/
    └── HoneyDuoGaming/            # Gaming app (legacy location)
```

**Ubuntu:**
```
/home/honey-duo/
├── honey-duo-infrastructure/     # Infrastructure configs
├── design-duo/                   # AI generation (Phase 1)
└── ira-trading-duo/              # Trading bots (Future)
```

---

## SSH Keys for GitHub

**Account-level SSH keys** (work for all repos):

**Pi:** `~/.ssh/id_ed25519_new` (no passphrase)  
**Ubuntu:** `~/.ssh/id_ed25519_new` (no passphrase)

Both added to GitHub account settings (not per-repo deploy keys).

---

## Giving Claude Access

**Why this structure exists:**

Claude can access GitHub repositories to:
- Review code and provide suggestions
- Understand full context of projects
- Help debug issues with access to actual code
- Provide accurate integration guidance
- See commit history and understand changes

**How to share code with Claude:**

1. **For quick questions:**
   - Share the GitHub URL: `https://github.com/HoneyDuoDevelopments/repo-name`
   - Claude can browse public files

2. **For private repos (current setup):**
   - Share specific code snippets in conversation
   - OR add Claude's analysis tools as collaborator (if needed)
   - OR temporarily make repo public for review (then private again)

3. **For comprehensive review:**
   - Commit and push current code
   - Share GitHub URL with Claude
   - Claude can review entire codebase structure

**Best practice:**
- Commit and push code FREQUENTLY
- Keep README.md updated in each repo
- Add comments to complex code
- This gives Claude maximum context to help you

---

## Workflow for New Repositories

When creating a new project repository:

1. **Create on GitHub** (via web interface)
2. **Clone locally** (on appropriate system)
3. **Add to this document** (REPOSITORIES.md)
4. **Create integration folder** in infrastructure repo
5. **Document in infrastructure** (pi/ or ubuntu/ directory)
6. **First commit** with basic structure
7. **Share with Claude** for initial review

See: `docs/github-workflow.md` → "Adding New Repositories"

---

## Repository Maintenance

**Weekly:**
- Review commit activity across all repos
- Ensure all repos have recent commits (if active development)
- Check that infrastructure docs match actual deployments

**Monthly:**
- Review and update this REPOSITORIES.md
- Verify all SSH keys still working
- Check for any stale branches

**When starting new project:**
- Create GitHub repo FIRST
- Update this document IMMEDIATELY
- Set up integration folder in infrastructure repo
- Document before coding (makes Claude more helpful)

---

## Quick Reference

**All repositories:**
```bash
# Infrastructure
cd ~/honey-duo-infrastructure && git pull

# Gaming (Pi only)
cd ~/Desktop/HoneyDuoGaming && git pull

# DesignDuo (Ubuntu only - Phase 1)
cd ~/design-duo && git pull

# TradingDuo (Ubuntu only - Future)
cd ~/ira-trading-duo && git pull
```

**GitHub organization:**
https://github.com/HoneyDuoDevelopments

---

**Last Updated:** December 31, 2025  
**Maintained By:** Sam  
**Review Frequency:** Weekly during active development
