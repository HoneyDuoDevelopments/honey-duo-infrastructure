# HoneyDuo Gaming - N64 Emulation Integration

**Code Repository:** https://github.com/HoneyDuoDevelopments/honey-duo-gaming  
**Actual Location:** `/home/honeyduopi/Desktop/HoneyDuoGaming`  
**Status:** ✅ Running

---

## Overview

Web-based control interface for RetroArch N64 emulation. Allows remote game launching, save state management, and cheat code support via web browser.

**External Access:** https://games.honey-duo.com (Cloudflare tunnel)

---

## Service Management

### Systemd Service

**Service Name:** `honeyduo-gaming.service`  
**Location:** `/etc/systemd/system/honeyduo-gaming.service`
```bash
# Check status
systemctl status honeyduo-gaming

# Restart service
sudo systemctl restart honeyduo-gaming

# View logs
journalctl -u honeyduo-gaming -f

# Stop service
sudo systemctl stop honeyduo-gaming

# Start service
sudo systemctl start honeyduo-gaming
```

---

## Configuration

### Service Configuration
```ini
[Unit]
Description=HoneyDuo Gaming Flask App
After=network.target

[Service]
User=honeyduopi
WorkingDirectory=/home/honeyduopi/Desktop/HoneyDuoGaming
Environment="PATH=/home/honeyduopi/Desktop/HoneyDuoGaming/venv/bin"
ExecStart=/home/honeyduopi/Desktop/HoneyDuoGaming/venv/bin/python app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Application Settings

- **Port:** 5000 (internal)
- **External Access:** https://games.honey-duo.com
- **ROM Directory:** `/home/honeyduopi/Desktop/HoneyDuoGaming/N64`
- **Log File:** `/home/honeyduopi/Desktop/HoneyDuoGaming/flask.log`

---

## Monitoring Integration

### Uptime Kuma (Phase 0 - Component 3)

**Monitor Configuration:**
- **Type:** HTTP(s)
- **URL:** http://localhost:5001
- **Interval:** 60 seconds
- **Alert on:** Service down

### Prometheus Metrics (Phase 0 - Component 4)

**Endpoint:** http://192.168.0.193:5001/health (to be added)

**Metrics to collect:**
- Request count
- Response time
- Active sessions
- Error rate

### Loki Logs (Phase 0 - Component 5)

**Log Files to Ship:**
- `/home/honeyduopi/Desktop/HoneyDuoGaming/flask.log`
- systemd journal: `honeyduo-gaming.service`

**Promtail Configuration:** See `../exporters/promtail-config.yml`

---

## Cloudflare Tunnel Integration

**Tunnel Configuration:** `/etc/cloudflared/config.yml`
```yaml
ingress:
  - hostname: games.honey-duo.com
    service: http://localhost:5001
```

**To update tunnel:**
```bash
sudo systemctl restart cloudflared
sudo systemctl status cloudflared
```

---

## Development

### Code Repository

**GitHub:** https://github.com/HoneyDuoDevelopments/honey-duo-gaming

**Clone for development:**
```bash
git clone git@github.com:HoneyDuoDevelopments/honey-duo-gaming.git
cd honey-duo-gaming
```

### Local Development
```bash
# Navigate to app directory
cd /home/honeyduopi/Desktop/HoneyDuoGaming

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
pip install -r requirements.txt

# Run in development mode
python app.py

# Deactivate venv
deactivate
```

### Making Changes

1. Make changes in `/home/honeyduopi/Desktop/HoneyDuoGaming`
2. Test locally
3. Commit to GitHub:
```bash
   cd /home/honeyduopi/Desktop/HoneyDuoGaming
   git add .
   git commit -m "Description of changes"
   git push
```
4. Restart service: `sudo systemctl restart honeyduo-gaming`

---

## Troubleshooting

### Service Won't Start
```bash
# Check service status
systemctl status honeyduo-gaming

# View detailed logs
journalctl -u honeyduo-gaming -n 50

# Check if port 5001 is in use
sudo ss -tlnp | grep :5001

# Verify venv exists
ls -la /home/honeyduopi/Desktop/HoneyDuoGaming/venv/
```

### Can't Access Externally
```bash
# Check Cloudflare tunnel
sudo systemctl status cloudflared

# Check local access first
curl -I http://localhost:5001

# Check tunnel logs
sudo journalctl -u cloudflared -n 50
```

### RetroArch Not Launching Games
```bash
# Check RetroArch is installed
which retroarch

# Check ROM permissions
ls -la /home/honeyduopi/Desktop/HoneyDuoGaming/N64/

# Manually launch RetroArch to test
retroarch -L /path/to/core.so /path/to/rom.z64
```

---

## Hardware Details

- **Raspberry Pi 5:** 8GB RAM, 2.8GHz overclock
- **Display:** 70-inch Samsung 4K TV (forced 1080p via xrandr)
- **Controllers:** 4x Aftermarket Bluetooth N64 controllers
- **Cooling:** Active PWM fan
- **Storage:** 500GB NVMe (PCIe Gen 2)

---

## Future Enhancements (Phase 1+)

- [ ] Add `/health` endpoint for Prometheus
- [ ] Implement structured logging (JSON)
- [ ] Add metrics for game launch count
- [ ] Add API for programmatic game launching
- [ ] Integrate with Grafana dashboard
- [ ] Add authentication (currently open)

---

## Related Documentation

- [Cloudflare Tunnel Setup](../../docs/cloudflare-tunnel-setup.md)
- [Monitoring Integration](../../docs/monitoring-integration.md)
- [Troubleshooting Guide](../../docs/troubleshooting.md)
