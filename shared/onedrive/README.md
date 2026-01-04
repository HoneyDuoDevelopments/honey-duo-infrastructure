# OneDrive Integration via rclone

Cloud backup storage for all Honey Duo systems.

**Status:** ✅ Running on Pi  
**Mount Point:** `/home/honeyduopi/OneDrive`  
**Service:** `rclone-onedrive.service`

---

## Backup Directory Structure
```
OneDrive/Backups/
├── Vaultwarden/     # Daily Vaultwarden database backups
├── Pi/              # Pi system configs and data
└── Ubuntu/          # Ubuntu system configs and data
```

---

## Service Management
```bash
# Check status
sudo systemctl status rclone-onedrive

# Restart if needed
sudo systemctl restart rclone-onedrive

# View logs
tail -f /var/log/rclone-onedrive.log

# Check if mounted
ls -la /home/honeyduopi/OneDrive/
```

---

## Configuration

**rclone config location:** `~/.config/rclone/rclone.conf`

**Systemd service:** `/etc/systemd/system/rclone-onedrive.service`

**Mount options:**
- `--vfs-cache-mode full` - Full file caching for reliability
- `--vfs-cache-max-age 24h` - Cache files for 24 hours
- `--dir-cache-time 72h` - Cache directory listings for 72 hours
- `--log-file /var/log/rclone-onedrive.log` - Logging location

---

## Manual Operations

**Copy file to OneDrive (without mount):**
```bash
rclone copy /local/file onedrive:Backups/Pi/
```

**Sync folder to OneDrive:**
```bash
rclone sync /local/folder onedrive:Backups/Pi/folder-name
```

**List OneDrive contents:**
```bash
rclone lsd onedrive:
rclone ls onedrive:Backups/
```

---

## Troubleshooting

### Mount not working
```bash
# Check service status
sudo systemctl status rclone-onedrive

# Check logs
tail -50 /var/log/rclone-onedrive.log

# Try manual mount
rclone mount onedrive: /home/honeyduopi/OneDrive --vfs-cache-mode full
```

### Authentication expired
```bash
# Re-authenticate
rclone config reconnect onedrive:
```

### Mount point busy
```bash
# Force unmount
sudo fusermount -uz /home/honeyduopi/OneDrive

# Restart service
sudo systemctl restart rclone-onedrive
```

---

## Ubuntu Setup (Future)

To set up OneDrive on Ubuntu system:

1. Install rclone: `sudo apt install rclone`
2. Copy config from Pi: `~/.config/rclone/rclone.conf`
3. Create mount point: `mkdir -p /home/honey-duo/OneDrive`
4. Copy systemd service (adjust paths for Ubuntu user)
5. Enable and start service

---

## Integration Points

- **Vaultwarden:** Daily automated backups to `Backups/Vaultwarden/`
- **Infrastructure Configs:** Manual backups to `Backups/Pi/` and `Backups/Ubuntu/`
- **Future:** Grafana dashboard exports, database dumps

---

**Last Updated:** January 4, 2026  
**Installed On:** Raspberry Pi 5
