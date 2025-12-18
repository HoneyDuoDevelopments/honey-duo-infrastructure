# Ubuntu Services

All services deployed on Ubuntu RTX 3090 system (192.168.0.245)

## Existing Services (Pre-Phase 0)

### honey-duo-web Monitoring App
- **Location:** `/home/honey-duo/webUI/honey-duo-web`
- **Purpose:** Basic GPU and system monitoring
- **Ports:** Frontend 3000, Backend 3001
- **Access:** https://honey-duo.com (Cloudflare tunnel)
- **Status:** ✅ Running
- **Future:** Will coexist with Grafana, eventually deprecated

## Phase 0 New Services

### Prometheus (Port 9090)
- **Location:** `~/honey-duo-infrastructure/ubuntu/monitoring/prometheus/`
- **Purpose:** Metrics collection and storage
- **Config:** `monitoring/prometheus/prometheus.yml`
- **Retention:** 30 days
- **Scrape Interval:** 15 seconds
- **Access:** http://192.168.0.245:9090 (VPN only)

### Grafana (Port 3000)
- **Location:** `~/honey-duo-infrastructure/ubuntu/monitoring/grafana/`
- **Purpose:** Metrics visualization and dashboards
- **Access:** http://192.168.0.245:3000 (VPN only)
- **Config:** `monitoring/grafana/`
- **Dashboards:** Stored in `monitoring/grafana/dashboards/`

### Loki (Port 3100)
- **Location:** `~/honey-duo-infrastructure/ubuntu/monitoring/loki/`
- **Purpose:** Log aggregation and storage
- **Config:** `monitoring/loki/loki-config.yml`
- **Retention:** 7 days
- **Access:** Internal only (scraped by Grafana)

### Alertmanager (Port 9093)
- **Location:** `~/honey-duo-infrastructure/ubuntu/monitoring/alertmanager/`
- **Purpose:** Alert routing to Discord
- **Config:** `monitoring/alertmanager/alertmanager.yml`
- **Access:** Internal only

### Web Terminal - ttyd (Port 7682)
- **Purpose:** Emergency shell access via browser
- **Access:** https://terminal-ubuntu.honey-duo.com (2FA required)
- **Config:** `/etc/systemd/system/ttyd-ubuntu.service`

### Exporters
- **Node Exporter (Port 9100):** System metrics
- **GPU Exporter (Port 9101):** RTX 3090 metrics
- **Promtail:** Log shipping to Loki

## Deployment
```bash
cd ~/honey-duo-infrastructure/ubuntu/monitoring
docker-compose up -d
```

## Maintenance

See [Ubuntu Maintenance Guide](../docs/ubuntu-maintenance.md)
