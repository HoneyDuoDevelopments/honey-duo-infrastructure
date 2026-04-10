# Ubuntu Services

All services deployed on Ubuntu RTX 3090 system (192.168.0.245)

## Current Status

The Ubuntu system is prepared for Phase 0 monitoring stack and Phase 1 GPU workloads.

## Cloudflare Tunnel (Ready for Future Services)

**Tunnel ID:** 2f0be609-2dee-4e1a-be2f-c8f83648421e  
**Config:** `/etc/cloudflared/config.yml`

Currently no active routes - ready for:
```yaml
ingress:
  # Phase 0
  - hostname: monitor.honey-duo.com  → localhost:3000 (Grafana)
  
  # Phase 1  
  - hostname: design.honey-duo.com   → localhost:8188 (DesignDuo/ComfyUI)
  
  # Future
  - hostname: ira.honey-duo.com      → localhost:xxxx (IRA Trading)
```

## Phase 0 Services (Coming)

### Prometheus (Port 9090)
- **Purpose:** Metrics collection and storage
- **Retention:** 30 days
- **Scrapes:** Both Pi and Ubuntu metrics

### Grafana (Port 3000)
- **Purpose:** Metrics visualization and dashboards
- **Access:** https://monitor.honey-duo.com (VPN recommended)

### Loki (Port 3100)
- **Purpose:** Log aggregation and storage
- **Retention:** 7 days

### Alertmanager (Port 9093)
- **Purpose:** Alert routing to Discord

### Exporters
- Node Exporter (Port 9100) - System metrics
- GPU Exporter (Port 9101) - RTX 3090 metrics
- Promtail - Log shipping to Loki

## Phase 1 Services (Planned)

### DesignDuo / ComfyUI (Port 8188)
- **Purpose:** AI image generation for Sticker Duo
- **GPU:** RTX 3090 (24GB VRAM)
- **Access:** https://design.honey-duo.com

| 5433 | PostgreSQL (Duo Wealth Test) | 🚧 Phase 1A |
| 5434 | PostgreSQL (Duo Wealth Prod) | 🔜 After validation |

## Future Services

### IRA Trading
- **Purpose:** Automated trading algorithms
- **Status:** Planning phase

## Quick Commands
```bash
# Check tunnel status
sudo systemctl status cloudflared

# Restart tunnel
sudo systemctl restart cloudflared

# Check GPU
nvidia-smi

# Check what's listening
ss -tlnp
```

## Adding New Services

See [Integration Guide](../docs/integration-guide.md)

## Maintenance

See [Ubuntu Maintenance Guide](../docs/ubuntu-maintenance.md)
