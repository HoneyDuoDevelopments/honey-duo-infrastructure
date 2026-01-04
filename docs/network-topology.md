# Network Topology

## Current Network
```
Internet
    │
ISP Modem
    │
TP-Link Archer Router (192.168.0.1)
    ├── DHCP: 192.168.0.100-249 (router managed)
    ├── DNS: 192.168.0.193 (Pi-hole)
    │
    ├── Raspberry Pi 5 (192.168.0.193) - Static IP - Ethernet
    │   ├── Pi-hole (DNS)
    │   ├── Cloudflare Tunnel → pi.honey-duo.com
    │   └── Phase 0 services
    │
    └── Ubuntu RTX 3090 (192.168.0.245) - DHCP (stable) - Ethernet
        ├── honey-duo-web app
        ├── Cloudflare Tunnel → honey-duo.com
        └── Phase 0 services
```

## VPN Network (Phase 0)
```
VPN Network: 10.8.0.0/24
    ├── 10.8.0.1 - VPN Server (Pi)
    ├── 10.8.0.2 - Laptop
    ├── 10.8.0.3 - Phone
    └── 10.8.0.4+ - Future devices
```

## Port Summary

**Raspberry Pi (192.168.0.193):**
| Port | Service | Access |
|------|---------|--------|
| 22 | SSH | Internal + VPN |
| 53 | Pi-hole DNS | Internal |
| 80 | Pi-hole Web | Internal + VPN |
| 5000 | Flask Gaming | Cloudflare |
| 8080 | Vaultwarden (Phase 0) | Cloudflare |
| 3001 | Uptime Kuma (Phase 0) | Internal + VPN |
| 51820/UDP | WireGuard (Phase 0) | Internet |

**Ubuntu (192.168.0.245):**
| Port | Service | Access |
|------|---------|--------|
| 22 | SSH | Internal + VPN |
| 3000 | Grafana (Phase 0) | VPN only |
| 3001 | Express Backend | Cloudflare |
| 9090 | Prometheus (Phase 0) | Internal |

*Detailed port mappings in Phase 0 master document.*
