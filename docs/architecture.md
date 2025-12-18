# Infrastructure Architecture

## Design Principles

1. **Separation of Concerns:** Pi = always-on services, Ubuntu = heavy compute
2. **Infrastructure as Code:** All configs in Git
3. **Defense in Depth:** Multiple security layers
4. **Observability First:** Metrics, logs, alerts everywhere
5. **Family Enablement:** Multi-user from day 1

## System Roles

**Raspberry Pi 5 (192.168.0.193):**
- DNS (Pi-hole)
- Secrets Management (Vaultwarden)
- Service Monitoring (Uptime Kuma)
- VPN Gateway (WireGuard)
- Network services that must stay up

**Ubuntu RTX 3090 (192.168.0.245):**
- Heavy compute workloads
- Metrics aggregation (Prometheus)
- Visualization (Grafana)
- Log aggregation (Loki)
- GPU-intensive tasks (ComfyUI - Phase 1)

*Full architecture documentation will be completed during Phase 0 implementation.*
