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
    └── Ubuntu RTX 3090 (192.168.0.245) - DHCP - Ethernet
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

*Detailed port mappings and service topology will be documented during Phase 0.*
