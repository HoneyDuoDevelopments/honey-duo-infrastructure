# Honey Duo — Repository Index

**Organization:** https://github.com/HoneyDuoDevelopments  
**Last Updated:** May 2026  
**Maintained By:** Sam

---

## Active Repositories

### honey-duo-infrastructure
**URL:** https://github.com/HoneyDuoDevelopments/honey-duo-infrastructure  
**Purpose:** Infrastructure configs, documentation, service setup guides for the entire hive  
**Systems:** Raspberry Pi 5 · Ubuntu RTX 3090 · Windows nodes  
**Status:** ✅ Active — continuously updated  

---

### Budget-Duo
**URL:** https://github.com/HoneyDuoDevelopments/Budget-Duo  
**Purpose:** Self-hosted household finance and budgeting app — Teller banking API integration  
**System:** Ubuntu RTX 3090  
**Location:** `~/Budget-Duo`  
**Live at:** https://budget.honey-duo.com  
**Stack:** FastAPI · PostgreSQL 16 · React (no build step)  
**Status:** ✅ Live — V4.1.1

**Services:**
- `budget-duo-backend` — FastAPI on `:8500`
- `budget-duo-db` — PostgreSQL on `:5432`

**Integration:**
- Cloudflare tunnel → `budget.honey-duo.com`
- Cloudflare Access — email OTP
- Credentials in Vaultwarden → Infrastructure

---

### honey-duo-gaming
**URL:** https://github.com/HoneyDuoDevelopments/honey-duo-gaming  
**Purpose:** Gaming hub — currently Pi-based N64 controller, expanding to multi-system cloud gaming  
**System:** Raspberry Pi 5 (current) · 3070 Ti + 1070 Windows nodes (expanding)  
**Location:** `/home/honeyduopi/Desktop/HoneyDuoGaming` (Pi)  
**Live at:** https://games.honey-duo.com  
**Status:** 🚧 Active — expanding to Moonlight/Sunshine multi-system setup

**Planned expansion:**
- Sunshine streaming host on 3070 Ti and 1070
- GameCube · N64 · PS2 · Steam emulation on 3070 Ti
- ROM file share from 3070 Ti to 1070
- Revamped games.honey-duo.com UI

---

### Duo-Wealth
**URL:** https://github.com/HoneyDuoDevelopments/Duo-Wealth  
**Purpose:** Algorithmic trading strategy incubator — research, backtest, validate, deploy  
**System:** Ubuntu RTX 3090  
**Location:** `~/Duo-Wealth`  
**Status:** 🚧 Active — Phase 1A Data Foundation

**Services:**
- PostgreSQL test instance `:5433`
- PostgreSQL prod instance `:5434`

**Integration:**
- Credentials in Vaultwarden → Infrastructure → "Duo Wealth DB"
- See: `ubuntu/duo-wealth/README.md`

---

### DataDuo
**URL:** https://github.com/HoneyDuoDevelopments/DataDuo  
**Purpose:** Market data pipeline — cloud deployment, enrichment API  
**System:** Ubuntu RTX 3090  
**Status:** 🚧 Active — early stage

---

## Archived Repositories

### design-duo
**URL:** https://github.com/HoneyDuoDevelopments/design-duo  
**Purpose:** Local AI image generation using ComfyUI / Stable Diffusion XL  
**Status:** 🗄️ **Archived — May 2026**  
**Reason:** GPT image generation now produces superior results for all household use cases. Local SDXL inference no longer justified given GPU memory and disk cost on the 3090. Codebase and model weights removed from Ubuntu to free resources for Duo Wealth and DataDuo.  
**Note:** Repository preserved for reference. Do not reinstall.

---

### ira-trading-duo
**URL:** https://github.com/HoneyDuoDevelopments/ira-trading-duo  
**Purpose:** Early trading bot placeholder  
**Status:** 🗄️ **Archived — superseded by Duo-Wealth**  
**Reason:** Duo Wealth is the full realization of this concept with proper architecture. IRA trading functionality will be a phase within Duo Wealth, not a separate repo.  
**Note:** Repository preserved for reference only.

---

## Planned Repositories

### sticker-duo (Concept)
**Purpose:** E-commerce platform for custom stickers  
**System:** TBD  
**Status:** 💡 Concept phase  
**Will integrate with:** Cloudflare tunnels · Vaultwarden · Monitoring stack

---

## System → Repository Map

| System | Repositories |
|--------|-------------|
| Raspberry Pi 5 | honey-duo-infrastructure · honey-duo-gaming |
| Ubuntu RTX 3090 | honey-duo-infrastructure · Budget-Duo · Duo-Wealth · DataDuo |
| 3070 Ti (coming) | honey-duo-gaming (Sunshine/emulation expansion) |
| 1070 (coming) | honey-duo-gaming (Moonlight client) |
| All systems | honey-duo-infrastructure |

---

## SSH Keys for GitHub

Both systems use account-level SSH keys (work for all repos):

**Pi:** `~/.ssh/id_ed25519_new`  
**Ubuntu:** `~/.ssh/id_ed25519_new`  

Added to GitHub account settings — not per-repo deploy keys.

---

## Quick Reference

```bash
# Infrastructure (Pi or Ubuntu)
cd ~/honey-duo-infrastructure && git pull

# Budget Duo (Ubuntu)
cd ~/Budget-Duo && git pull

# Gaming (Pi)
cd ~/Desktop/HoneyDuoGaming && git pull

# Duo Wealth (Ubuntu)
cd ~/Duo-Wealth && git pull

# DataDuo (Ubuntu)
cd ~/DataDuo && git pull
```