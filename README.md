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

## System Inventory

### Raspberry Pi 5 (192.168.0.193)
- **Hardware:** 8GB RAM, 500GB NVMe
- **Role:** Always-on network services
- **Services:**
  - Pi-hole (DNS + Ad Blocking) - `/home/honeyduopi/Pi-hole`
  - Flask Gaming App - `/home/honeyduopi/Desktop/HoneyDuoGaming`
  - Vaultwarden (Password Manager) - Phase 0
  - Uptime Kuma (Service Monitoring) - Phase 0
  - WireGuard VPN (Secure Access) - Phase 0
  - Web Terminal (Emergency Access) - Phase 0

### Ubuntu RTX 3090 (192.168.0.245)
- **Hardware:** i9-9900KF, 31GB RAM, RTX 3090 24GB VRAM
- **Role:** Heavy compute + monitoring aggregation
- **Services:**
  - honey-duo-web (Existing Monitor) - `/home/honey-duo/webUI/honey-duo-web`
  - Prometheus (Metrics Collection) - Phase 0
  - Grafana (Dashboards) - Phase 0
  - Loki (Log Aggregation) - Phase 0
  - Alertmanager (Alert Routing) - Phase 0
  - Web Terminal (Emergency Access) - Phase 0

## Documentation

- [Architecture Overview](docs/architecture.md)
- [Network Topology](docs/network-topology.md)
- [Disaster Recovery](docs/disaster-recovery.md)
- [Operational Runbooks](docs/RUNBOOKS.md)
- [Integration Guide](docs/integration-guide.md)
- [Troubleshooting](docs/troubleshooting.md)

## External Access

- **Vaultwarden:** https://vault.honey-duo.com (Phase 0)
- **Uptime Kuma:** https://status.honey-duo.com (Phase 0)
- **Web Terminals:** https://terminal-pi.honey-duo.com (Phase 0, 2FA required)
- **Grafana:** VPN only (http://192.168.0.245:3000) (Phase 0)

## Repository Structure
```
honey-duo-infrastructure/
├── docs/              # All documentation
├── pi/                # Raspberry Pi configs
├── ubuntu/            # Ubuntu system configs
└── shared/            # Common scripts/configs
```

## Emergency Contacts

**Owner:** Sam  
**Alerts:** Discord #honey-duo-alerts (Phase 0)
**Emergency Access:** Wife has admin credentials in Vaultwarden (Phase 0)

## Current Phase

**Phase 0:** Infrastructure Foundation (IN PROGRESS)
- [ ] Component 1: GitHub Repository ← YOU ARE HERE
- [ ] Component 2: Vaultwarden Multi-User Setup
- [ ] Component 3: Uptime Kuma Service Monitoring
- [ ] Component 4: Prometheus & Grafana Stack
- [ ] Component 5: Loki & Promtail Logging
- [ ] Component 6: WireGuard VPN
- [ ] Component 7: Web Terminal Access
- [ ] Component 8: Documentation & Runbooks

## License

Private - Family Use Only
