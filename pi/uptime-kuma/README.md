# Uptime Kuma - Service Monitoring

**URL:** https://status.honey-duo.com  
**Public Status:** https://status.honey-duo.com/status/dashboard  
**Port:** 3001  
**Status:** ✅ Running

## Overview

Service availability monitoring with Discord alerts for all Honey Duo services.

## Service Management
```bash
cd ~/honey-duo-infrastructure/pi/uptime-kuma

# Status
docker compose ps

# Restart
docker compose restart

# Logs
docker compose logs -f

# Update
docker compose pull
docker compose up -d
```

## Monitors

| Service | Type | URL/Target |
|---------|------|------------|
| Portal | HTTP | https://honey-duo.com |
| Gaming | HTTP | https://games.honey-duo.com |
| Vaultwarden | HTTP | https://vault.honey-duo.com |
| Pi-hole Web | HTTP | https://pihole.honey-duo.com/admin |
| Pi-hole DNS | DNS | 192.168.0.193:53 |
| Pi System | Ping | 192.168.0.193 |
| Ubuntu System | Ping | 192.168.0.245 |

## Notifications

- **Discord:** #honey-duo-alerts channel
- **Webhook:** Stored in Vaultwarden → Infrastructure → "Discord - Honey Duo Alerts"

## Admin Access

- **URL:** https://status.honey-duo.com
- **Credentials:** Vaultwarden → Infrastructure → "Uptime Kuma Admin"

## Public Status Page

- **URL:** https://status.honey-duo.com/status/dashboard
- Shows service availability without requiring login

## Backup

Data stored in `./data/` directory.
