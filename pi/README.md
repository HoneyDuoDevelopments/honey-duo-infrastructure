# Raspberry Pi Services

All services deployed on Raspberry Pi 5 (192.168.0.193)

## Live Services

### Portal (Port 5000)
- **Location:** `/home/honeyduopi/portal`
- **Purpose:** Central service dashboard
- **Access:** https://honey-duo.com
- **Service:** `honeyduo-portal.service`
- **Docs:** [pi/portal/README.md](portal/README.md)

### Gaming (Port 5001)
- **Location:** `/home/honeyduopi/Desktop/HoneyDuoGaming`
- **Purpose:** N64 emulation web control
- **Access:** https://games.honey-duo.com
- **Service:** `honeyduo-gaming.service`
- **Docs:** [pi/gaming/README.md](gaming/README.md)

### Vaultwarden (Port 8080)
- **Location:** `~/honey-duo-infrastructure/pi/vaultwarden/`
- **Purpose:** Self-hosted password manager
- **Access:** https://vault.honey-duo.com
- **Service:** Docker containers
- **Docs:** [pi/vaultwarden/README.md](vaultwarden/README.md)

### Pi-hole (Port 53, 80)
- **Location:** System-wide (`/etc/pihole/`)
- **Purpose:** DNS + network-wide ad blocking
- **Access:** https://pihole.honey-duo.com/admin
- **Service:** `pihole-FTL.service`
- **Docs:** [pi/pi-hole/README.md](pi-hole/README.md)

## Phase 0 Services (Coming)

### Uptime Kuma (Port 3001)
- **Purpose:** Service monitoring with Discord alerts
- **Access:** https://status.honey-duo.com
- **Docs:** [pi/uptime-kuma/README.md](uptime-kuma/README.md)

### WireGuard VPN (Port 51820 UDP)
- **Purpose:** Secure remote access to home network
- **Docs:** [pi/wireguard/README.md](wireguard/README.md)

## Cloudflare Tunnel

**Tunnel ID:** fe770a64-3546-4bc5-99c3-7f9726cf84e3  
**Config:** `/etc/cloudflared/config.yml`

Current routes:
```yaml
ingress:
  - hostname: honey-duo.com        → localhost:5000 (Portal)
  - hostname: games.honey-duo.com  → localhost:5001 (Gaming)
  - hostname: vault.honey-duo.com  → localhost:8080 (Vaultwarden)
  - hostname: pihole.honey-duo.com → localhost:80 (Pi-hole)
```

## Quick Commands
```bash
# Check all services
sudo systemctl status honeyduo-portal honeyduo-gaming pihole-FTL cloudflared

# Restart a service
sudo systemctl restart honeyduo-portal

# View logs
journalctl -u honeyduo-portal -f

# Check tunnel
sudo systemctl status cloudflared
```

## Maintenance

See [Pi Maintenance Guide](../docs/pi-maintenance.md)
