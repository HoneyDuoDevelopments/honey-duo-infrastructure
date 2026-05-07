# Network Topology

**Last Updated:** May 2026

---

## External Access Architecture

```
Internet
    │
    ▼
Cloudflare (Proxy + SSL + Access)
    │
    ├── honey-duo.com ──────────┐
    ├── games.honey-duo.com ────┤
    ├── vault.honey-duo.com ────┼──▶ Pi Tunnel (fe770a64-3546-4bc5-99c3-7f9726cf84e3)
    ├── pihole.honey-duo.com ───┤         │
    ├── status.honey-duo.com ───┘         ▼
    │                              Raspberry Pi (192.168.0.193)
    │
    ├── monitor.honey-duo.com ───┐
    ├── code.honey-duo.com ──────┤
    └── budget.honey-duo.com ────┼──▶ Ubuntu Tunnel (2f0be609-2dee-4e1a-be2f-c8f83648421e)
                                 │         │
                                 │         ▼
                                 │  Ubuntu RTX 3090 (192.168.0.245)
                                 │
                        (All protected by Cloudflare Access — email OTP)
```

---

## Internal Network — `192.168.0.0/24`

```
TP-Link Archer Router (192.168.0.1)
├── DHCP Pool: 192.168.0.100–249
├── DNS: 192.168.0.193 (Pi-hole)
│
├── Raspberry Pi 5 (192.168.0.193) — Static (DHCP reservation)
│   ├── Pi-hole       :53 / :80
│   ├── Portal        :5000
│   ├── Gaming        :5001
│   ├── Vaultwarden   :8080
│   ├── Uptime Kuma   :3001
│   ├── NoMachine     :4000
│   └── Cloudflare Tunnel (outbound only)
│
├── Ubuntu RTX 3090 (192.168.0.245) — Static (DHCP reservation)
│   ├── Grafana        :3000
│   ├── Prometheus     :9090
│   ├── Loki           :3100
│   ├── Alertmanager   :9093
│   ├── Code Server    :8443
│   ├── Budget Duo     :8500
│   ├── Budget Duo DB  :5432
│   ├── Duo Wealth DB  :5433 (test) / :5434 (prod)
│   ├── WireGuard VPN  :51820 UDP (planned)
│   └── Cloudflare Tunnel (outbound only)
│
├── GTX 1070 Gaming Node (192.168.0.137) — Static (DHCP reservation)
│   ├── Sunshine       :47990
│   ├── PCSX2          (local)
│   ├── Dolphin        (local)
│   ├── RetroArch      (local)
│   └── Steam          (local)
│
├── RTX 3070 Ti Gaming Hub (192.168.0.244) — Static (DHCP reservation)
│   ├── Sunshine       :47990
│   ├── ROM share      (Samba, planned)
│   └── Steam          (local)
│
└── Windows Laptop (DHCP)
    ├── WireGuard client
    └── Moonlight client
```

---

## DHCP Reservations

All static IPs are managed via DHCP reservation in the TP-Link Archer router (no per-host static config).

| IP | Hostname | MAC | Notes |
|---|---|---|---|
| 192.168.0.137 | gtx-1070-gaming-node | *(TBD — capture from router)* | Sunshine streaming + emulation |
| 192.168.0.193 | honeyduo-pi58gb | *(TBD — capture from router)* | Pi 5 — always-on services |
| 192.168.0.244 | rtx-3070-ti-gaming-hub | `30-C5-99-74-8B-E2` | Primary gaming host + ROM server |
| 192.168.0.245 | honey-duo-MS-7B98 | *(TBD — capture from router)* | Ubuntu — compute + monitoring |

> **Action item:** capture remaining MACs from TP-Link reservation list and fill in this table.

---

## VPN Network — `10.8.0.0/24` *(planned)*

```
WireGuard Server: Ubuntu RTX 3090 (:51820 UDP)

10.8.0.1 — Ubuntu RTX 3090 (server)
10.8.0.2 — Raspberry Pi 5
10.8.0.3 — Windows Laptop
10.8.0.4 — RTX 3070 Ti Gaming Hub
10.8.0.5 — GTX 1070 Gaming Node
10.8.0.6 — Phone (mobile)
```

**Mode:** Split tunnel — only `10.8.0.0/24` and `192.168.0.0/24` routed through VPN  
**DNS via VPN:** Pi-hole at `192.168.0.193` — local `.home` names resolve remotely  
**Tool:** wg-easy (Docker) on Ubuntu 3090

---

## Subdomain Routing

| Subdomain | Target | Port | System | Status |
|-----------|--------|------|--------|--------|
| honey-duo.com | Portal | 5000 | Pi | ✅ Live |
| games.honey-duo.com | Gaming Hub | 5001 | Pi | ✅ Live |
| vault.honey-duo.com | Vaultwarden | 8080 | Pi | ✅ Live |
| pihole.honey-duo.com | Pi-hole | 80 | Pi | ✅ Live |
| status.honey-duo.com | Uptime Kuma | 3001 | Pi | ✅ Live |
| monitor.honey-duo.com | Grafana | 3000 | Ubuntu | ✅ Live |
| code.honey-duo.com | Code Server | 8443 | Ubuntu | ✅ Live |
| budget.honey-duo.com | Budget Duo | 8500 | Ubuntu | ✅ Live |
| design.honey-duo.com | DesignDuo | — | — | 🗄️ Archived |
| ira.honey-duo.com | IRA Trading | — | — | 🗄️ Archived |

---

## Cloudflare Tunnels

### Pi Tunnel
- **ID:** `fe770a64-3546-4bc5-99c3-7f9726cf84e3`
- **Config:** `/etc/cloudflared/config.yml`
- **Handles:** honey-duo.com · games · vault · pihole · status

### Ubuntu Tunnel
- **ID:** `2f0be609-2dee-4e1a-be2f-c8f83648421e`
- **Config:** `/etc/cloudflared/config.yml`
- **Handles:** monitor · code · budget

---

## Port Summary

### External (Internet-Facing)
All traffic proxied through Cloudflare tunnels — **no inbound ports open on router** for web services.  
Only planned external port forward: `51820 UDP → 192.168.0.245` (WireGuard VPN, pending)

### Internal Services — Pi (`192.168.0.193`)
| Port | Service |
|------|---------|
| 53 | Pi-hole DNS |
| 80 | Pi-hole web UI |
| 3001 | Uptime Kuma |
| 4000 | NoMachine |
| 5000 | Portal |
| 5001 | Gaming Hub |
| 8080 | Vaultwarden |

### Internal Services — Ubuntu (`192.168.0.245`)
| Port | Service |
|------|---------|
| 3000 | Grafana |
| 3100 | Loki |
| 5432 | Budget Duo PostgreSQL |
| 5433 | Duo Wealth DB (test) |
| 5434 | Duo Wealth DB (prod) |
| 8443 | Code Server |
| 8500 | Budget Duo API |
| 9090 | Prometheus |
| 9093 | Alertmanager |
| 51820 | WireGuard VPN (planned) |

### Internal Services — GTX 1070 (`192.168.0.137`)
| Port | Service |
|------|---------|
| 47990 | Sunshine web UI + pairing |

### Internal Services — RTX 3070 Ti (`192.168.0.244`)
| Port | Service |
|------|---------|
| 47990 | Sunshine web UI + pairing |
| 445 | Samba ROM share (planned) |