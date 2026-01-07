# Network Topology

## Current Architecture (January 2026)
```
Internet
    │
    ▼
Cloudflare (Proxy + SSL)
    │
    ├── honey-duo.com ──────────┐
    ├── games.honey-duo.com ────┤
    ├── vault.honey-duo.com ────┼──▶ Pi Tunnel ──▶ Raspberry Pi (192.168.0.193)
    ├── pihole.honey-duo.com ───┤
    ├── status.honey-duo.com ───┘    (future)
    │
    ├── monitor.honey-duo.com ──┐
    ├── design.honey-duo.com ───┼──▶ Ubuntu Tunnel ──▶ Ubuntu RTX 3090 (192.168.0.245)
    └── ira.honey-duo.com ──────┘    (future)
```

## Internal Network (192.168.0.0/24)
```
TP-Link Archer Router (192.168.0.1)
├── DHCP Server: 192.168.0.100-249
├── DNS Server: 192.168.0.193 (Pi-hole)
│
├── Raspberry Pi 5 (192.168.0.193) - Static IP
│   ├── Pi-hole (DNS + Ad Blocking)
│   ├── Portal (:5000)
│   ├── Gaming (:5001)
│   ├── Vaultwarden (:8080)
│   ├── Uptime Kuma (:3001) [Phase 0]
│   ├── WireGuard VPN (:51820) [Phase 0]
│   └── Cloudflare Tunnel
│
└── Ubuntu RTX 3090 (192.168.0.245) - DHCP (stable)
    ├── Prometheus (:9090) [Phase 0]
    ├── Grafana (:3000) [Phase 0]
    ├── Loki (:3100) [Phase 0]
    ├── Alertmanager (:9093) [Phase 0]
    ├── DesignDuo/ComfyUI (:8188) [Phase 1]
    └── Cloudflare Tunnel
```

## VPN Network (Phase 0)
```
WireGuard VPN: 10.8.0.0/24
├── 10.8.0.1 - VPN Server (Pi)
├── 10.8.0.2 - Laptop
├── 10.8.0.3 - Phone
└── 10.8.0.4+ - Future devices
```

## Subdomain Routing

| Subdomain | Target | Port | System | Status |
|-----------|--------|------|--------|--------|
| honey-duo.com | Portal | 5000 | Pi | ✅ Live |
| games.honey-duo.com | Gaming | 5001 | Pi | ✅ Live |
| vault.honey-duo.com | Vaultwarden | 8080 | Pi | ✅ Live |
| pihole.honey-duo.com | Pi-hole | 80 | Pi | ✅ Live |
| status.honey-duo.com | Uptime Kuma | 3001 | Pi | 🔜 Phase 0 |
| monitor.honey-duo.com | Grafana | 3000 | Ubuntu | 🔜 Phase 0 |
| design.honey-duo.com | DesignDuo | 8188 | Ubuntu | 🔜 Phase 1 |
| ira.honey-duo.com | IRA Trading | TBD | Ubuntu | 🔜 Future |

## Cloudflare Tunnels

### Pi Tunnel
- **ID:** fe770a64-3546-4bc5-99c3-7f9726cf84e3
- **Config:** /etc/cloudflared/config.yml
- **Handles:** All current production services

### Ubuntu Tunnel
- **ID:** 2f0be609-2dee-4e1a-be2f-c8f83648421e
- **Config:** /etc/cloudflared/config.yml
- **Handles:** Future GPU/compute services

## Port Summary

### External (Internet-Facing via Cloudflare)
- All traffic proxied through Cloudflare tunnels
- No direct port forwarding required
- SSL terminated at Cloudflare

### Future: WireGuard VPN
- Port 51820 UDP - Only external port forward needed
- Provides direct network access when remote

## Updated Routes (January 2026)

### Ubuntu Tunnel Routes
- monitor.honey-duo.com → Grafana (Port 3000) ✅ Active
