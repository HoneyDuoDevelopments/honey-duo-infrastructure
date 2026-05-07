# Infrastructure Architecture

**Last Updated:** May 2026

---

## Design Principles

1. **Separation of Concerns:** Pi = always-on lightweight services, Ubuntu = heavy compute and databases, Windows = gaming and streaming
2. **Infrastructure as Code:** All configs and documentation in Git
3. **Defense in Depth:** Cloudflare Access → Cloudflare Tunnels → UFW → application-level auth
4. **Observability First:** Metrics, logs, and alerts on every system
5. **Family Enablement:** Multi-user, role-based access from day one
6. **Self-Sufficient:** No critical external service dependencies — VPN, DNS, secrets all self-hosted

---

## System Roles

### Raspberry Pi 5 — `192.168.0.193`
Always-on lightweight services. Never goes down intentionally.
- DNS and network-wide ad blocking (Pi-hole)
- Secrets management (Vaultwarden)
- Service monitoring (Uptime Kuma)
- Portal dashboard (Flask)
- Gaming hub UI (Flask)
- Cloudflare tunnel for all Pi-hosted web services

### Ubuntu RTX 3090 — `192.168.0.245`
Heavy compute, databases, monitoring stack, active development.
- Metrics aggregation (Prometheus)
- Visualization (Grafana)
- Log aggregation (Loki + Promtail)
- Alert routing (Alertmanager)
- Browser-based development (Code Server)
- Household finance app (Budget Duo — FastAPI + PostgreSQL)
- Trading strategy incubator (Duo Wealth — PostgreSQL)
- Market data pipeline (DataDuo)
- WireGuard VPN server (planned — `10.8.0.0/24`)
- Cloudflare tunnel for all Ubuntu-hosted web services

### Windows Laptop — DHCP
Mobile development and remote access.
- Primary dev workstation
- WireGuard VPN client
- Moonlight streaming client

### GTX 1070 Gaming Node — `192.168.0.137`
Dedicated emulation and streaming box.
- Sunshine streaming host (NVENC hardware encoder)
- PS2 emulation (PCSX2)
- GameCube / Wii emulation (Dolphin)
- PS1 + N64 emulation (RetroArch)
- Steam gaming

### RTX 3070 Ti Gaming Hub — `192.168.0.244`
Primary gaming host and ROM server.
- Sunshine streaming host
- Central ROM library (shared to 1070 via Samba — planned)
- GameCube / N64 / PS2 emulation
- Steam gaming
- **Hardware:** Ryzen 5 5500, ASUS Prime B550M-A WIFI II, 16GB DDR4-3200, RTX 3070 Ti, 750W PSU, ASUS Prime AP201 case

---

## Security Architecture

```
Internet
    │
    ▼
Cloudflare Access (Layer 1)
Email OTP — only approved addresses reach the tunnel
    │
    ▼
Cloudflare Tunnel (Layer 2)
Encrypted egress — no inbound ports open on router
    │
    ▼
Application (Layer 3)
Service-level auth where applicable
    │
    ▼
UFW Firewall (Layer 4)
Internal services locked to LAN or VPN subnet only
```

**Credentials:** All secrets in Vaultwarden. Nothing hardcoded, nothing in Git.  
**VPN:** WireGuard on Ubuntu 3090 — hub-and-spoke, split tunnel, `10.8.0.0/24`

---

## Monitoring Architecture

```
All systems
    │ node_exporter (Linux) / windows_exporter (Windows)
    ▼
Prometheus (Ubuntu :9090)
    │ scrapes every 15s
    ├──▶ Grafana (Ubuntu :3000) — dashboards and visualization
    └──▶ Alertmanager (Ubuntu :9093) — alert routing → Discord

All systems
    │ Promtail
    ▼
Loki (Ubuntu :3100) — log aggregation
    │
    └──▶ Grafana — log exploration

All services
    │ HTTP/TCP health checks
    ▼
Uptime Kuma (Pi :3001) — uptime and status page
```

---

## Archived Systems

### Design Duo *(Archived May 2026)*
- **Was:** Local AI image generation — ComfyUI / Stable Diffusion XL on Ubuntu RTX 3090
- **Why archived:** GPT image generation produces superior results for all household use cases. Local SDXL inference no longer justified given GPU memory and disk cost.
- **Action taken:** Codebase and model weights removed from Ubuntu. GPU memory and disk freed for Duo Wealth and DataDuo.
- **Repository:** Preserved on GitHub for reference. Do not reinstall.

### IRA Trading Duo *(Archived — superseded)*
- **Was:** Early trading bot placeholder repository
- **Why archived:** Fully superseded by Duo Wealth, which is the proper realization of this concept with a complete architecture.
- **Repository:** Preserved on GitHub for reference only.

---

## Future Architecture (Phase 1 targets)

- WireGuard VPN mesh across all 5 nodes
- ~~Static IP reservations for all nodes in router~~ ✅ Complete (May 2026)
- Pi-hole local DNS hostnames (`.home` domain)
- Unbound recursive DNS (no upstream provider)
- windows_exporter on both Windows gaming nodes → Prometheus
- Samba ROM share from 3070 Ti to 1070
- Moonlight / Sunshine cloud gaming network