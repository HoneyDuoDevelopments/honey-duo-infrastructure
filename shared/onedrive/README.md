# OneDrive Integration via rclone

Cloud backup storage for all Honey Duo systems.

---

## System Status

| System | Status | Mount Point | Service |
|--------|--------|-------------|---------|
| Raspberry Pi | ✅ Running | `/home/honeyduopi/OneDrive` | `rclone-onedrive.service` |
| Ubuntu | ✅ Running | `/home/honey-duo/OneDrive-rclone` | `rclone-onedrive.service` |

---

## Backup Directory Structure
```
OneDrive/Backups/
├── Vaultwarden/     # Daily Vaultwarden database backups (from Pi)
├── Pi/              # Pi system configs and data
└── Ubuntu/          # Ubuntu system configs and data
```

---

## Service Management

### Raspberry Pi
```bash
# Check status
sudo systemctl status rclone-onedrive

# Restart
sudo systemctl restart rclone-onedrive

# View logs
tail -f /var/log/rclone-onedrive.log

# Check mount
ls -la /home/honeyduopi/OneDrive/
```

### Ubuntu
```bash
# Check status
sudo systemctl status rclone-onedrive

# Restart
sudo systemctl restart rclone-onedrive

# View logs
tail -f /var/log/rclone-onedrive.log

# Check mount
ls -la /home/honey-duo/OneDrive-rclone/
```

---

## Configuration Files

### rclone config
- **Pi:** `~/.config/rclone/rclone.conf`
- **Ubuntu:** `~/.config/rclone/rclone.conf`

Both use the same Microsoft authentication token.

### Systemd service
- **Both systems:** `/etc/systemd/system/rclone-onedrive.service`

### Mount options (both systems)
- `--vfs-cache-mode full` - Full file caching for reliability
- `--vfs-cache-max-age 24h` - Cache files for 24 hours
- `--dir-cache-time 72h` - Cache directory listings for 72 hours
- `--log-file /var/log/rclone-onedrive.log` - Logging location

---

## Manual Operations

**Copy file to OneDrive:**
```bash
rclone copy /local/file onedrive:Backups/Pi/
```

**Sync folder to OneDrive:**
```bash
rclone sync /local/folder onedrive:Backups/Ubuntu/folder-name
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

# Try manual mount (Pi)
rclone mount onedrive: /home/honeyduopi/OneDrive --vfs-cache-mode full

# Try manual mount (Ubuntu)
rclone mount onedrive: /home/honey-duo/OneDrive-rclone --vfs-cache-mode full
```

### Authentication expired
```bash
# Re-authenticate (run on one system, copy config to other)
rclone config reconnect onedrive:
```

### Mount point busy
```bash
# Force unmount (Pi)
sudo fusermount -uz /home/honeyduopi/OneDrive

# Force unmount (Ubuntu)
sudo fusermount -uz /home/honey-duo/OneDrive-rclone

# Restart service
sudo systemctl restart rclone-onedrive
```

---

## Integration Points

- **Vaultwarden:** Daily automated backups to `Backups/Vaultwarden/`
- **Infrastructure Configs:** Manual backups to `Backups/Pi/` and `Backups/Ubuntu/`
- **Future:** Grafana dashboard exports, database dumps

---

## Notes

### Ubuntu Legacy OneDrive Client
Ubuntu previously had the native `onedrive` client installed (abraunegg/onedrive).
This has been disabled in favor of rclone for consistency across both systems.

The old sync folder remains at `/home/honey-duo/OneDrive` but is no longer actively synced.
The new rclone mount is at `/home/honey-duo/OneDrive-rclone`.

A symlink exists: `/home/honey-duo/OneDrive-Cloud -> /home/honey-duo/OneDrive-rclone`

---

**Last Updated:** January 4, 2026  
**Installed On:** Raspberry Pi 5, Ubuntu RTX 3090
