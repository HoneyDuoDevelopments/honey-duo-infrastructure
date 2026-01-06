# Honey Duo Portal

**Location:** `/home/honeyduopi/portal`  
**URL:** https://honey-duo.com  
**Port:** 5000  
**Status:** ✅ Running

## Overview

Central entry point for all Honey Duo services. Password-protected dashboard with links to all subdomains.

## Service Management
```bash
sudo systemctl status honeyduo-portal
sudo systemctl restart honeyduo-portal
journalctl -u honeyduo-portal -f
```

## Configuration

- **Systemd Service:** `/etc/systemd/system/honeyduo-portal.service`
- **Environment:** `/home/honeyduopi/portal/.env`
- **Password:** Vaultwarden → "HoneyDuo Portal"

## Adding Services to Portal

Edit `/home/honeyduopi/portal/app.py` and add to `SERVICES` dict, then:
```bash
sudo systemctl restart honeyduo-portal
```

## Current Services

| Service | Subdomain | Port |
|---------|-----------|------|
| Portal | honey-duo.com | 5000 |
| Gaming | games.honey-duo.com | 5001 |
| Vaultwarden | vault.honey-duo.com | 8080 |
| Pi-hole | pihole.honey-duo.com | 80 |
