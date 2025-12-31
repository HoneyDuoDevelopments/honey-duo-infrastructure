# Pi-hole Integration

**Installation:** System-wide (apt package)  
**Config Location:** `/etc/pihole/`  
**Status:** ✅ Running

---

## Overview

Network-wide DNS server with ad blocking. Currently blocking 41.3% of ads across entire home network.

**Web Interface:** http://192.168.0.193/admin  
**DNS Server:** 192.168.0.193:53

---

## Installation Locations

Pi-hole is installed **system-wide**, not in the infrastructure repo.

### Key Directories
```
/etc/pihole/              # Main configuration
├── gravity.db            # Blocklist database
├── pihole-FTL.db         # Query database
├── pihole.toml           # Main config
└── setupVars.conf        # Installation settings

/opt/pihole/              # Pi-hole scripts
/usr/local/bin/pihole     # Pi-hole CLI
/var/log/pihole/          # Logs (FTL, queries)
```

### Source Code Clone

`/home/honeyduopi/Pi-hole/` contains the Pi-hole source code repository (cloned from GitHub). This is **NOT** the actual installation - it can be deleted if needed.

**Actual Pi-hole installation** is in `/etc/pihole/` and `/opt/pihole/`.

---

## Service Management

### Pi-hole FTL Service

**Service Name:** `pihole-FTL.service`
```bash
# Status
systemctl status pihole-FTL

# Restart Pi-hole
sudo systemctl restart pihole-FTL

# View logs
journalctl -u pihole-FTL -f

# Stop/Start
sudo systemctl stop pihole-FTL
sudo systemctl start pihole-FTL
```

### Pi-hole CLI
```bash
# Status summary
pihole status

# Restart DNS
pihole restartdns

# Update gravity (blocklists)
pihole -g

# Enable/disable blocking
pihole enable
pihole disable

# Query a domain
pihole -q google.com

# Tail query log
pihole -t
```

---

## Configuration

### Current Settings

- **DNS Port:** 53 (UDP/TCP)
- **Web Interface Port:** 80
- **DHCP:** Disabled (router handles DHCP)
- **DNS Provider:** Router manages, points to Pi-hole
- **Admin Interface:** http://192.168.0.193/admin
- **Blocking:** Enabled (41.3% of queries blocked)

### Network Configuration

**Router Settings (TP-Link Archer):**
- **DHCP Server:** Router (192.168.0.1)
- **DNS Server:** 192.168.0.193 (Pi-hole)
- **Static IP for Pi:** 192.168.0.193

**Why DHCP on Router:**
- Reliability: Network continues if Pi-hole down
- Single point of failure eliminated
- DNS is non-critical service (degrades gracefully)

---

## Monitoring Integration

### Uptime Kuma (Phase 0 - Component 3)

**Monitor Configuration:**
- **Type:** HTTP(s) + DNS
- **HTTP URL:** http://192.168.0.193/admin
- **DNS Query:** google.com via 192.168.0.193
- **Interval:** 60 seconds

### Prometheus Metrics (Phase 0 - Component 4)

**Future:** Install pi-hole-exporter
- **GitHub:** https://github.com/eko/pihole-exporter
- **Metrics:** Queries, blocks, clients, upstream queries

### Loki Logs (Phase 0 - Component 5)

**Log Files to Ship:**
- `/var/log/pihole/FTL.log`
- `/var/log/pihole/pihole.log`
- systemd journal: `pihole-FTL.service`

**Promtail Configuration:** See `../exporters/promtail-config.yml`

---

## Maintenance

### Update Pi-hole
```bash
# Update Pi-hole core + web interface
pihole -up

# Check current version
pihole -v
```

### Update Blocklists
```bash
# Manual update
pihole -g

# Automatic updates: Configured via cron (daily)
```

### Backup Configuration
```bash
# Create backup (via web interface)
# Settings → Teleporter → Backup

# Or via CLI
sudo tar -czf ~/pihole-backup-$(date +%Y%m%d).tar.gz /etc/pihole/

# Copy to OneDrive
cp ~/pihole-backup-*.tar.gz /home/honeyduopi/OneDrive/Backups/Pi-hole/
```

### Restore Configuration
```bash
# Via web interface:
# Settings → Teleporter → Restore

# Or manually:
sudo tar -xzf pihole-backup-YYYYMMDD.tar.gz -C /
sudo systemctl restart pihole-FTL
```

---

## Customization

### Custom Blocklists

Add via: **Settings → Adlists** in web interface

**Current Lists:**
- Default Pi-hole lists
- Additional lists (view in `/etc/pihole/adlists.list`)

### Whitelist/Blacklist
```bash
# Whitelist a domain
pihole -w example.com

# Blacklist a domain  
pihole -b badsite.com

# Regex whitelist
pihole --white-regex '.*\.example\.com$'

# View lists
pihole -w -l
pihole -b -l
```

---

## Troubleshooting

### DNS Not Resolving
```bash
# Check Pi-hole status
pihole status

# Check FTL service
systemctl status pihole-FTL

# Test DNS resolution
nslookup google.com 192.168.0.193

# Check if port 53 is listening
sudo ss -tlnp | grep :53

# Restart DNS
pihole restartdns
```

### Web Interface Not Loading
```bash
# Check lighttpd (web server)
systemctl status lighttpd

# Restart web server
sudo systemctl restart lighttpd

# Check port 80
sudo ss -tlnp | grep :80

# Check Pi-hole FTL (serves web interface)
systemctl status pihole-FTL
```

### High Memory Usage
```bash
# Check FTL database size
ls -lh /etc/pihole/pihole-FTL.db

# Flush query database (if too large)
sudo pihole -f

# Restart FTL
sudo systemctl restart pihole-FTL
```

---

## Integration with Infrastructure

### Current

- DNS for entire network (41.3% blocking)
- Accessible at http://192.168.0.193/admin
- Running as systemd service

### Phase 0 Integration

1. **Component 3:** Uptime Kuma monitoring (HTTP + DNS checks)
2. **Component 4:** Prometheus metrics (via pi-hole-exporter)
3. **Component 5:** Logs shipped to Loki
4. **Component 6:** Accessible via VPN when remote

### Future Enhancements

- [ ] Install pi-hole-exporter for Prometheus
- [ ] Create Grafana dashboard for Pi-hole stats
- [ ] Automated backup to OneDrive (daily)
- [ ] Alert on high query failure rate
- [ ] Track blocking effectiveness over time

---

## Admin Credentials

**Admin Password:** Stored in Vaultwarden (Component 2)  
**Collection:** Infrastructure  
**Item Name:** "Pi-hole Admin"

**Reset password if needed:**
```bash
pihole -a -p
# Enter new password when prompted
```

---

## Related Documentation

- [Network Topology](../../docs/network-topology.md)
- [DNS Configuration](../../docs/dns-configuration.md)
- [Monitoring Integration](../../docs/monitoring-integration.md)
