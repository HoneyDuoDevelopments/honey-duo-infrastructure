# Ubuntu Cloudflare Tunnel

**Tunnel ID:** 2f0be609-2dee-4e1a-be2f-c8f83648421e  
**Config:** `/etc/cloudflared/config.yml`  
**Credentials:** `/home/honey-duo/.cloudflared/2f0be609-2dee-4e1a-be2f-c8f83648421e.json`

## Active Routes

| Subdomain | Target | Port | Service |
|-----------|--------|------|---------|
| monitor.honey-duo.com | localhost:3000 | 3000 | Grafana |

## Future Routes (Phase 1+)

| Subdomain | Target | Port | Service |
|-----------|--------|------|---------|
| design.honey-duo.com | localhost:8188 | 8188 | DesignDuo/ComfyUI |
| ira.honey-duo.com | localhost:TBD | TBD | IRA Trading |

## Service Management
```bash
# Check status
sudo systemctl status cloudflared

# Restart tunnel
sudo systemctl restart cloudflared

# View logs
sudo journalctl -u cloudflared -f

# Test config syntax
cloudflared tunnel ingress validate
```

## Adding New Services

1. Update `/etc/cloudflared/config.yml`
2. Add DNS CNAME in Cloudflare: `<subdomain>` → `2f0be609-2dee-4e1a-be2f-c8f83648421e.cfargotunnel.com`
3. Restart tunnel: `sudo systemctl restart cloudflared`
4. Flush Pi-hole DNS: `pihole reloaddns` (on Pi)
5. Test: `curl -I https://<subdomain>.honey-duo.com`

## Current Config

See: `/etc/cloudflared/config.yml`
