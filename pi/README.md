# Raspberry Pi Services

All services deployed on Raspberry Pi 5 (192.168.0.193)

## Existing Services (Pre-Phase 0)

### Pi-hole (Port 53, 80)
- **Location:** `/home/honeyduopi/Pi-hole`
- **Purpose:** DNS + network-wide ad blocking
- **Access:** http://192.168.0.193/admin
- **Status:** ✅ Running
- **Integration:** Configs in `pi/pi-hole/`

### Flask Gaming App (Port 5000)
- **Location:** `/home/honeyduopi/Desktop/HoneyDuoGaming/app.py`
- **Purpose:** N64 emulation web control
- **Access:** https://pi.honey-duo.com (Cloudflare tunnel)
- **Status:** ✅ Running
- **Integration:** Monitoring configs in this repo

### OneDrive Mount
- **Location:** `/home/honeyduopi/OneDrive`
- **Purpose:** Cloud backup integration
- **Status:** ✅ Mounted
- **Used by:** Vaultwarden backups (Phase 0)

## Phase 0 New Services

### Vaultwarden (Port 8080)
- **Location:** `~/honey-duo-infrastructure/pi/vaultwarden/`
- **Purpose:** Self-hosted password manager
- **Access:** https://vault.honey-duo.com
- **Config:** `vaultwarden/docker-compose.yml`
- **Data:** Backed up daily to OneDrive

### Uptime Kuma (Port 3001)
- **Location:** `~/honey-duo-infrastructure/pi/uptime-kuma/`
- **Purpose:** Service monitoring with Discord alerts
- **Access:** http://192.168.0.193:3001
- **Config:** `uptime-kuma/docker-compose.yml`

### WireGuard VPN (Port 51820 UDP)
- **Location:** `/etc/wireguard/wg0.conf`
- **Purpose:** Secure remote access to home network
- **VPN Network:** 10.8.0.0/24
- **Configs:** `wireguard/`

### Web Terminal - ttyd (Port 7681)
- **Purpose:** Emergency shell access via browser
- **Access:** https://terminal-pi.honey-duo.com (2FA required)
- **Config:** `/etc/systemd/system/ttyd-pi.service`

### Exporters
- **Node Exporter (Port 9100):** System metrics for Prometheus
- **Promtail:** Log shipping to Loki

## Deployment

**Existing services:** Already running, documented only  
**New services:** Deployed via Docker Compose or systemd during Phase 0

## Maintenance

See [Pi Maintenance Guide](../docs/pi-maintenance.md)
