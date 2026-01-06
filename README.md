# Honey Duo Infrastructure

Production-grade self-hosted infrastructure for all Honey Duo services.

**Owner:** Sam  
**Systems:** Raspberry Pi 5 + Ubuntu RTX 3090  
**Purpose:** Foundation for Sticker Duo, trading bots, and all future services

## Quick Start

**First-time setup:**
1. Clone this repository to both systems
2. Follow [Phase 0 Setup Guide](docs/Phase-0-Setup.md)
3. Review [Integration Guide](docs/integration-guide.md) before adding services

## Live Services

| Service | URL | System |
|---------|-----|--------|
| Portal | https://honey-duo.com | Pi |
| Gaming | https://games.honey-duo.com | Pi |
| Vaultwarden | https://vault.honey-duo.com | Pi |
| Pi-hole | https://pihole.honey-duo.com/admin | Pi |

## System Inventory

### Raspberry Pi 5 (192.168.0.193)
- **Hardware:** 8GB RAM, 500GB NVMe, 2.8GHz overclock
- **Role:** Always-on network services + Portal
- **Services:**
  - Portal (Service Dashboard)
  - Pi-hole (DNS + Ad Blocking)
  - Vaultwarden (Password Manager)
  - Gaming (N64 Emulation)
  - Uptime Kuma (Phase 0)
  - WireGuard VPN (Phase 0)

### Ubuntu RTX 3090 (192.168.0.245)
- **Hardware:** i9-9900KF, 31GB RAM, RTX 3090 24GB VRAM
- **Role:** Heavy compute + monitoring aggregation
- **Services:**
  - Prometheus + Grafana (Phase 0)
  - Loki (Phase 0)
  - DesignDuo/ComfyUI (Phase 1)
  - IRA Trading (Future)

## Documentation

- [Architecture Overview](docs/architecture.md)
- [Network Topology](docs/network-topology.md)
- [Integration Guide](docs/integration-guide.md) ← **Read before adding services**
- [Disaster Recovery](docs/disaster-recovery.md)
- [Operational Runbooks](docs/RUNBOOKS.md)
- [Troubleshooting](docs/troubleshooting.md)

## Repository Structure
```
honey-duo-infrastructure/
├── docs/              # All documentation
├── pi/                # Raspberry Pi configs
│   ├── portal/        # Service dashboard
│   ├── gaming/        # N64 emulation
│   ├── vaultwarden/   # Password manager
│   ├── pi-hole/       # DNS + ad blocking
│   ├── uptime-kuma/   # Service monitoring (Phase 0)
│   └── wireguard/     # VPN (Phase 0)
├── ubuntu/            # Ubuntu system configs
│   ├── monitoring/    # Prometheus/Grafana/Loki (Phase 0)
│   ├── design-duo/    # AI image generation (Phase 1)
│   └── ira-trading-duo/ # Trading bots (Future)
├── shared/            # Common scripts/configs
└── github/            # Repository references
```

## Current Phase

**Phase 0:** Infrastructure Foundation (IN PROGRESS)
- [x] Component 1: GitHub Repository ✅
- [x] Component 2: Vaultwarden Multi-User Setup ✅
- [ ] Component 3: Uptime Kuma Service Monitoring ← NEXT
- [ ] Component 4: Prometheus & Grafana Stack
- [ ] Component 5: Loki & Promtail Logging
- [ ] Component 6: WireGuard VPN
- [ ] Component 7: Web Terminal Access
- [ ] Component 8: Documentation & Runbooks

## Emergency Contacts

**Owner:** Sam  
**Alerts:** Discord #honey-duo-alerts (Phase 0)  
**Emergency Access:** Wife has admin credentials in Vaultwarden

## License

Private - Family Use Only
