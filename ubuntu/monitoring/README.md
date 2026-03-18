# Monitoring Stack - Prometheus, Grafana, Alertmanager

**Status:** ✅ Running  
**System:** Ubuntu RTX 3090 (192.168.0.245)  
**Access:** VPN only (no public exposure)

---

## Services

### Prometheus (Port 9090)
- **Purpose:** Metrics collection and storage
- **URL:** http://192.168.0.245:9090
- **Retention:** 30 days
- **Scrape Interval:** 15s
- **Targets:** Pi (192.168.0.193:9100), Ubuntu (localhost:9100, localhost:9101)

### Grafana (Port 3000)
- **Purpose:** Metrics visualization
- **URL:** http://192.168.0.245:3000
- **Credentials:** Vaultwarden → Infrastructure → "Grafana Admin"
- **Dashboards:** 
  - System Overview (CPU, RAM for both systems)
  - GPU Monitoring (RTX 3090 stats)

### Alertmanager (Port 9093)
- **Purpose:** Alert routing to Discord
- **URL:** http://192.168.0.245:9093
- **Discord Webhook:** Vaultwarden → Infrastructure → "Discord - Honey Duo Alerts"

### Exporters
- **Node Exporter (9100):** System metrics (CPU, RAM, disk, network)
- **GPU Exporter (9101):** DCGM metrics (GPU temp, util, VRAM, power, clocks)

---

## Quick Commands
```bash
cd ~/honey-duo-infrastructure/ubuntu/monitoring

# Check status
docker compose ps

# View logs
docker compose logs -f
docker compose logs grafana -f
docker compose logs prometheus -f

# Restart services
docker compose restart
docker compose restart grafana

# Update images
docker compose pull
docker compose up -d
```

---

## Dashboards

### System Overview
- **UID:** honey-duo-system
- **Location:** `grafana/dashboards/system-overview.json`
- **Metrics:**
  - Pi & Ubuntu CPU usage (%)
  - Pi & Ubuntu memory usage (%)
  - CPU usage over time (both systems)
  - Memory available over time (both systems)

### GPU Monitoring  
- **UID:** honey-duo-gpu
- **Location:** `grafana/dashboards/gpu-monitoring.json`
- **Metrics:**
  - GPU temperature (°C)
  - GPU utilization (%)
  - VRAM utilization (%)
  - Power usage (W)
  - Temperature over time
  - GPU/VRAM utilization over time
  - Clock speeds (GPU & memory)

---

## Alert Rules

| Alert | Threshold | Duration | Severity |
|-------|-----------|----------|----------|
| ServiceDown | Service unreachable | 30s | critical |
| HighGPUTemp | >85°C | 1m | warning |
| HighCPU | >90% | 5m | warning |
| HighMemory | >90% | 5m | warning |
| HighDisk | >85% | 5m | warning |

All alerts sent to Discord #honey-duo-alerts channel.

---

## Resource Usage

**Idle (no workloads):**
- CPU: 10-15%
- Memory: ~1-1.5GB
- Disk: ~15GB (Prometheus data grows over time)

**Active (during queries/alerts):**
- CPU: 20-30%
- Memory: ~2GB

---

## Configuration Files
```
ubuntu/monitoring/
├── docker-compose.yml              # All services
├── .env                            # Secrets (gitignored)
├── prometheus/
│   ├── prometheus.yml              # Prometheus config
│   └── alerts/
│       └── infrastructure.yml      # Alert rules
├── grafana/
│   ├── dashboards/
│   │   ├── system-overview.json    # System dashboard
│   │   └── gpu-monitoring.json     # GPU dashboard
│   └── provisioning/
│       ├── datasources/
│       │   └── prometheus.yml      # Prometheus datasource
│       └── dashboards/
│           └── dashboards.yml      # Auto-load dashboards
├── alertmanager/
│   └── alertmanager.yml            # Alert routing config
└── discord-webhook-adapter/
    └── webhook-adapter.py          # Discord alert formatter
```

---

## Adding New Dashboards

1. Create JSON file in `grafana/dashboards/`
2. Use datasource UID: `PBFA97CFB590B2093`
3. Grafana auto-loads from `provisioning/dashboards/dashboards.yml`
4. Commit to Git

---

## Troubleshooting

### No data in Grafana
```bash
# Check Prometheus targets
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[]'

# Check if exporters running
curl http://localhost:9100/metrics | head
curl http://localhost:9101/metrics | head

# Check Grafana datasource
# Grafana UI → Connections → Data sources → Prometheus → Test
```

### Alerts not sending
```bash
# Check alertmanager logs
docker compose logs alertmanager -f

# Check Discord webhook adapter
docker compose logs discord-webhook-adapter -f

# Test webhook manually
curl -X POST http://localhost:5001/webhook \
  -H "Content-Type: application/json" \
  -d '{"status":"firing","alerts":[{"labels":{"alertname":"Test"}}]}'
```

### High resource usage
```bash
# Check per-container usage
docker stats --no-stream

# Reduce Prometheus retention if needed
# Edit prometheus.yml: --storage.tsdb.retention.time=15d
```

---

## Maintenance

**Daily:** Automated - no action needed

**Weekly:**
- Review dashboard metrics for trends
- Check Discord alerts for patterns

**Monthly:**
- Review Prometheus disk usage: `du -sh prometheus/data/`
- Update Docker images: `docker compose pull && docker compose up -d`

---

## Future Enhancements

- [ ] Add Loki for log aggregation (Component 5)
- [ ] Create dashboard for ComfyUI (Phase 1)
- [ ] Add custom metrics for trading bots
- [ ] Email alerts (in addition to Discord)
- [ ] Grafana Cloud backup (optional)

---

**Last Updated:** January 6, 2026  
**Component:** Phase 0 - Component 4  
**Next Component:** Loki & Promtail Logging
