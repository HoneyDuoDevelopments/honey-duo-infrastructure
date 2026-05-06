# Honey Duo Infrastructure

Production-grade self-hosted infrastructure for all Honey Duo services.

**Owner:** Sam  
**Systems:** Raspberry Pi 5 · Ubuntu RTX 3090 · Windows Laptop · 3070 Ti · 1070  
**Purpose:** Foundation for all Honey Duo services — gaming, finance, development, and future projects  
**Last Updated:** May 2026

---

## Quick Start

**First-time setup:**
1. Clone this repository to both systems
2. Follow [Phase 0 Setup Guide](docs/Phase-0-Setup.md)
3. Review [Integration Guide](docs/integration-guide.md) before adding services

---

## Live Services

| Service | URL | System |
|---------|-----|--------|
| Portal | https://honey-duo.com | Pi |
| Budget Duo | https://budget.honey-duo.com | Ubuntu |
| Gaming Hub | https://games.honey-duo.com | Pi |
| Vaultwarden | https://vault.honey-duo.com | Pi |
| Grafana | https://monitor.honey-duo.com | Ubuntu |
| Code Server | https://code.honey-duo.com | Ubuntu |
| System Status | https://status.honey-duo.com | Pi |
| Pi-hole | https://pihole.honey-duo.com/admin | Pi |

All external services are protected by Cloudflare Access (email OTP).

---

## System Inventory

### Raspberry Pi 5 — `192.168.0.193`
- **Hardware:** 8GB RAM · 500GB NVMe · 2.8GHz overclock
- **Role:** Always-on network services, portal, DNS
- **OS:** Raspberry Pi OS (64-bit)
- **Services:**
  - Portal (Flask — systemd) `:5000`
  - Pi-hole (DNS + Ad Blocking) `:53 / :80`
  - Vaultwarden (Password Manager) `:8080`
  - Gaming Hub (Flask — systemd) `:5001`
  - Uptime Kuma (Service Monitoring) `:3001`
  - NoMachine (Remote Desktop) `:4000`

### Ubuntu RTX 3090 — `192.168.0.245`
- **Hardware:** i9-9900KF · 31GB RAM · RTX 3090 24GB VRAM · 2TB NVMe
- **Role:** Heavy compute, monitoring stack, databases, active projects
- **OS:** Ubuntu 22.04 LTS
- **Services:**
  - Grafana (Dashboards) `:3000`
  - Prometheus (Metrics) `:9090`
  - Loki (Log Aggregation) `:3100`
  - Alertmanager (Alerts) `:9093`
  - Code Server (VSCode in Browser) `:8443`
  - Budget Duo (FastAPI + PostgreSQL) `:8500 / :5432`
  - Duo Wealth DB test `:5433`
  - Duo Wealth DB prod `:5434`

### Windows Laptop — DHCP
- **Role:** Dev workstation, remote access, Moonlight client
- **Services:** WireGuard client · Moonlight client

### 3070 Ti Gaming Hub — TBD IP *(coming online)*
- **Role:** Primary gaming host, ROM server, cloud gaming hub
- **OS:** Windows
- **Planned:** Sunshine (stream host) · GameCube / N64 / PS2 emulation · Steam · ROM file share

### GTX 1070 Gaming Node — `192.168.0.137`
- **Hardware:** i5-3550 · 16GB DDR3 · GTX 1070 8GB · 500GB SSD
- **Role:** Emulation node + Moonlight/Sunshine streaming host
- **OS:** Windows 10 Pro
- **Services:** Sunshine (stream host) · PCSX2 · Dolphin · RetroArch · Steam
- **Docs:** `windows/gaming-node-1070/README.md`

---

## Network

- **Router:** TP-Link Archer — `192.168.0.1`
- **DNS:** Pi-hole at `192.168.0.193` (network-wide)
- **VPN:** WireGuard on Ubuntu 3090 — planned subnet `10.8.0.0/24`
- **External access:** Cloudflare tunnels (Pi + Ubuntu) — no inbound ports exposed for web services
- **Port forward:** `51820 UDP → 192.168.0.245` (WireGuard, pending)

---

## Security Model

1. **Cloudflare Access** — email OTP gate on all external web services
2. **Cloudflare Tunnels** — no inbound port exposure for web services
3. **WireGuard VPN** — encrypted inter-device access (Ubuntu 3090 as server, planned)
4. **Vaultwarden** — all credentials stored here, never in code or plaintext files
5. **UFW** — firewall rules on Pi and Ubuntu (internal services LAN-only)

---

## Active Projects

| Project | System | URL | Status |
|---------|--------|-----|--------|
| Budget Duo | Ubuntu | https://budget.honey-duo.com | ✅ Live |
| Duo Wealth | Ubuntu | https://github.com/HoneyDuoDevelopments/Duo-Wealth | 🚧 Phase 1A |
| DataDuo | Ubuntu | https://github.com/HoneyDuoDevelopments/DataDuo | 🚧 Active |
| Gaming Hub | Pi + Windows | https://games.honey-duo.com | 🚧 Expanding |
| Design Duo | — | — | 🗄️ Archived |
| IRA Trading Duo | — | — | 🗄️ Superseded by Duo Wealth |

---

## Documentation

- [Architecture Overview](docs/architecture.md)
- [Network Topology](docs/network-topology.md)
- [Integration Guide](docs/integration-guide.md) ← **Read before adding services**
- [Disaster Recovery](docs/disaster-recovery.md)
- [Operational Runbooks](docs/RUNBOOKS.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Security Hardening](docs/security-hardening.md)
- [Phase 0 Setup Guide](docs/Phase-0-Setup.md)

---

## Repository Structure

```
honey-duo-infrastructure/
├── docs/                        # Architecture and operational docs
│   ├── architecture.md
│   ├── network-topology.md
│   ├── integration-guide.md
│   ├── disaster-recovery.md
│   ├── RUNBOOKS.md
│   ├── security-hardening.md
│   ├── Phase-0-Setup.md
│   └── troubleshooting.md
├── pi/                          # Raspberry Pi service configs and docs
│   ├── README.md
│   ├── portal/                  # Service dashboard
│   ├── gaming/                  # Gaming hub
│   ├── vaultwarden/             # Password manager
│   ├── pi-hole/                 # DNS + ad blocking
│   ├── uptime-kuma/             # Service monitoring
│   └── wireguard/               # VPN (planned)
├── ubuntu/                      # Ubuntu service configs and docs
│   ├── README.md
│   ├── monitoring/              # Prometheus · Grafana · Loki · Alertmanager
│   ├── budget-duo/              # Household finance app
│   ├── duo-wealth/              # Trading strategy incubator
│   └── data-duo/                # Market data pipeline
├── windows/                     # Windows node setup guides
│   ├── gaming-hub-3070/         # 3070 Ti setup (coming online)
│   └── gaming-node-1070/        # 1070 setup (coming online)
├── shared/                      # Common scripts and configs
└── github/                      # Repository references
    ├── REPOSITORIES.md
    └── github-workflow-guide.md
```

---

## Infrastructure Phase Tracker

### Phase 0 — Foundation ✅ Complete
- [x] GitHub Repository
- [x] Vaultwarden Multi-User Setup
- [x] Uptime Kuma Service Monitoring
- [x] Prometheus & Grafana Stack
- [x] Loki & Promtail Logging
- [x] Code Server (Web Terminal)
- [x] Cloudflare Tunnels (Pi + Ubuntu)
- [x] Portal with Cloudflare Access auth

### Phase 1 — Hive Expansion 🚧 In Progress
- [x] Budget Duo live
- [x] Duo Wealth — Phase 1A Data Foundation
- [x] DataDuo active
- [ ] WireGuard VPN (Ubuntu 3090 as server)
- [ ] Static IP reservations — all 5 nodes
- [ ] Pi-hole local DNS hostnames
- [ ] UFW audit and rules (Pi + Ubuntu)
- [ ] 3070 Ti gaming hub online
- [ ] 1070 gaming node online
- [ ] Moonlight / Sunshine cloud gaming setup
- [ ] windows_exporter monitoring for new nodes
- [ ] Unbound recursive DNS

### Phase 2 — Polish (Planned)
- [ ] Cloudflare Access on all internal tools
- [ ] GitHub Actions CI/CD for active projects
- [ ] Automated PostgreSQL backups
- [ ] Internal reverse proxy (Caddy)
- [ ] Local Docker registry

---

## Emergency

**Owner:** Sam · samuelosmith5@gmail.com  
**Backup admin:** Jessica · turtleelephant111422@gmail.com  
**Alerts:** Uptime Kuma → Discord #honey-duo-alerts  
**Credentials:** Vaultwarden → Infrastructure collection  
**Monitoring:** https://status.honey-duo.com

---

## License

Private — Family Use Only