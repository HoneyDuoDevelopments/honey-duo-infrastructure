# Integration Guide - Adding New Services

How to add new services to the Honey Duo infrastructure.

---

## Architecture Overview
```
Internet
    │
    ▼
Cloudflare (DNS + Proxy)
    │
    ├─── Pi Tunnel (fe770a64-...) ───┐
    │                                 │
    │    ┌────────────────────────────┴────────────────────────────┐
    │    │ Raspberry Pi (192.168.0.193)                            │
    │    │                                                          │
    │    │  honey-duo.com      → :5000 (Portal)                    │
    │    │  games.honey-duo.com → :5001 (Gaming)                   │
    │    │  vault.honey-duo.com → :8080 (Vaultwarden)              │
    │    │  pihole.honey-duo.com → :80 (Pi-hole)                   │
    │    │  status.honey-duo.com → :3001 (Uptime Kuma) [FUTURE]    │
    │    └─────────────────────────────────────────────────────────┘
    │
    └─── Ubuntu Tunnel (2f0be609-...) ───┐
                                          │
         ┌────────────────────────────────┴────────────────────────┐
         │ Ubuntu RTX 3090 (192.168.0.245)                         │
         │                                                          │
         │  monitor.honey-duo.com → :3000 (Grafana) [FUTURE]       │
         │  design.honey-duo.com  → :8188 (DesignDuo) [FUTURE]     │
         │  ira.honey-duo.com     → :xxxx (IRA Bot) [FUTURE]       │
         └─────────────────────────────────────────────────────────┘
```

---

## Adding a New Service - Step by Step

### Step 1: Deploy Your Service

Get your service running locally on the appropriate system (Pi or Ubuntu).
```bash
# Verify it's running
curl -I http://localhost:YOUR_PORT
```

### Step 2: Store Credentials in Vaultwarden

1. Go to https://vault.honey-duo.com
2. Add new Login item with service credentials
3. Place in "Infrastructure" collection

### Step 3: Add DNS Record (Cloudflare Dashboard)

1. Go to Cloudflare Dashboard → honey-duo.com → DNS
2. Add CNAME record:
   - **Name:** `yourservice`
   - **Target:** 
     - Pi services: `fe770a64-3546-4bc5-99c3-7f9726cf84e3.cfargotunnel.com`
     - Ubuntu services: `2f0be609-2dee-4e1a-be2f-c8f83648421e.cfargotunnel.com`
   - **Proxy:** ON (orange cloud)

### Step 4: Update Tunnel Config

**For Pi services** - edit `/etc/cloudflared/config.yml`:
```yaml
ingress:
  - hostname: yourservice.honey-duo.com
    service: http://localhost:YOUR_PORT
  # ... existing services ...
  - service: http_status:404
```

**For Ubuntu services** - edit `/etc/cloudflared/config.yml`:
```yaml
ingress:
  - hostname: yourservice.honey-duo.com
    service: http://localhost:YOUR_PORT
  - service: http_status:404
```

Then restart the tunnel:
```bash
sudo systemctl restart cloudflared
```

### Step 5: Flush DNS Cache
```bash
sudo pihole reloaddns
```

### Step 6: Add to Portal

Edit `/home/honeyduopi/portal/app.py` - add to appropriate section in `SERVICES` dict:
```python
{
    'name': 'Your Service',
    'description': 'What it does',
    'url': 'https://yourservice.honey-duo.com',
    'icon': '🔧',
    'color': '#hexcolor'
},
```

Restart portal:
```bash
sudo systemctl restart honeyduo-portal
```

### Step 7: Update Documentation

1. Create `pi/yourservice/README.md` or `ubuntu/yourservice/README.md`
2. Update `docs/network-topology.md`
3. Commit and push to GitHub

### Step 8: Add Monitoring (After Phase 0 Component 3)

Add to Uptime Kuma:
- HTTP check on `https://yourservice.honey-duo.com`
- Alert to Discord on failure

---

## Tunnel Reference

### Pi Tunnel
- **ID:** `fe770a64-3546-4bc5-99c3-7f9726cf84e3`
- **Config:** `/etc/cloudflared/config.yml`
- **Credentials:** `/etc/cloudflared/fe770a64-3546-4bc5-99c3-7f9726cf84e3.json`

### Ubuntu Tunnel  
- **ID:** `2f0be609-2dee-4e1a-be2f-c8f83648421e`
- **Config:** `/etc/cloudflared/config.yml`
- **Credentials:** `/home/honey-duo/.cloudflared/2f0be609-2dee-4e1a-be2f-c8f83648421e.json`

---

## Port Allocation

### Pi Ports (192.168.0.193)
| Port | Service | Status |
|------|---------|--------|
| 53 | Pi-hole DNS | ✅ Active |
| 80 | Pi-hole Web | ✅ Active |
| 3001 | Uptime Kuma | 🔜 Phase 0 |
| 4000 | NoMachine | ✅ Active |
| 5000 | Portal | ✅ Active |
| 5001 | Gaming | ✅ Active |
| 8080 | Vaultwarden | ✅ Active |
| 9100 | Node Exporter | 🔜 Phase 0 |
| 51820 | WireGuard | 🔜 Phase 0 |

### Ubuntu Ports (192.168.0.245)
| Port | Service | Status |
|------|---------|--------|
| 3000 | Grafana | 🔜 Phase 0 |
| 3100 | Loki | �� Phase 0 |
| 8188 | ComfyUI/DesignDuo | 🔜 Phase 1 |
| 9090 | Prometheus | 🔜 Phase 0 |
| 9093 | Alertmanager | 🔜 Phase 0 |
| 9100 | Node Exporter | 🔜 Phase 0 |
| 9101 | GPU Exporter | 🔜 Phase 0 |

---

## Checklist for New Services

- [ ] Service running locally
- [ ] Credentials in Vaultwarden
- [ ] DNS CNAME added in Cloudflare
- [ ] Tunnel config updated
- [ ] Tunnel restarted
- [ ] Pi-hole DNS flushed
- [ ] Portal updated (if user-facing)
- [ ] Documentation created
- [ ] Monitoring added (Uptime Kuma)
- [ ] Git committed and pushed
