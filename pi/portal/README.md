# Honey Duo Portal

**Live at:** https://honey-duo.com  
**Internal:** http://192.168.0.193:5000  
**System:** Raspberry Pi 5  
**Stack:** Flask · Python 3 · systemd  
**Last Updated:** May 2026

---

## What It Does

The portal is the central dashboard for the Honey Duo home network. It presents all active services as tiles, filtered by user role. Authentication is handled entirely by Cloudflare Access — no second login.

---

## Authentication Model

```
User visits honey-duo.com
        ↓
Cloudflare Access — email OTP gate
(only the 5 approved emails get through)
        ↓
Flask reads Cf-Access-Authenticated-User-Email header
Maps email → role → renders appropriate tiles
        ↓
Dashboard — no login page, no passwords
```

**Approved users and roles:**

| Name | Email | Role |
|------|-------|------|
| Sam | samuelosmith5@gmail.com | admin |
| Jessica | turtleelephant111422@gmail.com | admin |
| Deon | dragontaimerkevin@gmail.com | kids |
| Claudae | claudae.mclin@icloud.com | kids |
| Nyala | nyala.mclin@icloud.com | kids |

**Role visibility:**

| Category | admin | family | kids |
|----------|-------|--------|------|
| Home (Vault, Status, Budget) | ✅ | ✅ | ❌ |
| Gaming | ✅ | ✅ | ✅ |
| Monitoring (Grafana, Pi-hole) | ✅ | ❌ | ❌ |
| Infrastructure (Code Server, Vault Admin) | ✅ | ❌ | ❌ |
| Projects (Duo Wealth, DataDuo, Infra) | ✅ | ❌ | ❌ |

---

## File Structure

```
/home/honeyduopi/portal/
├── app.py                  ← Flask app — all tile definitions and auth logic
├── .secrets                ← Email/role mappings (chmod 600, never in Git)
├── requirements.txt        ← flask only
└── templates/
    ├── dashboard.html      ← Main portal UI
    ├── admin_users.html    ← Admin user list view (/admin/users)
    ├── 401.html            ← Direct access without Cloudflare header
    └── 403.html            ← Email not in approved list
```

---

## Service Management

```bash
# Status
sudo systemctl status honeyduo-portal

# Restart
sudo systemctl restart honeyduo-portal

# Logs
journalctl -u honeyduo-portal -f

# Logs (last 50 lines)
journalctl -u honeyduo-portal -n 50
```

---

## Configuration

All user config lives in `/home/honeyduopi/portal/.secrets` — injected by systemd `EnvironmentFile=`.

```bash
# View current users (no secrets exposed)
# Visit https://honey-duo.com/admin/users (admin only)

# Edit user config
nano /home/honeyduopi/portal/.secrets
sudo systemctl restart honeyduo-portal
```

**`.secrets` format:**
```
CF_USER_SAM_EMAIL=samuelosmith5@gmail.com
CF_USER_SAM_ROLE=admin
CF_USER_SAM_DISPLAY=Sam
```

**To add a user:**
1. Add their 3 lines to `.secrets`
2. Add their email to Cloudflare Access policy for `honey-duo.com`
3. `sudo systemctl restart honeyduo-portal`

**To change a role:**
1. Edit `CF_USER_<NAME>_ROLE` in `.secrets`
2. `sudo systemctl restart honeyduo-portal`

---

## Adding or Editing Tiles

Tiles are defined in `app.py` in the `TILE_CATEGORIES` list. Each tile has:

```python
{
    "name": "Service Name",
    "description": "Short description",
    "url": "https://service.honey-duo.com",
    "icon": "emoji or symbol",
    "accent": "#HexColor",
    "roles": ["admin", "family", "kids"],  # who can see it
}
```

After editing `app.py`: `sudo systemctl restart honeyduo-portal`

---

## systemd Service

**File:** `/etc/systemd/system/honeyduo-portal.service`

```ini
[Unit]
Description=HoneyDuo Portal Flask App
After=network.target

[Service]
User=honeyduopi
Group=honeyduopi
WorkingDirectory=/home/honeyduopi/portal
EnvironmentFile=/home/honeyduopi/portal/.secrets
Environment="PATH=/home/honeyduopi/portal/venv/bin"
ExecStart=/home/honeyduopi/portal/venv/bin/python app.py
Restart=always
RestartSec=5
NoNewPrivileges=yes
PrivateTmp=yes

[Install]
WantedBy=multi-user.target
```

---

## Cloudflare Integration

- **Tunnel:** Pi Cloudflare tunnel → `localhost:5000`
- **Access policy:** `honey-duo.com` — email OTP, 5 approved addresses
- **Managed at:** Cloudflare Zero Trust dashboard

**To add a new approved email:**
Cloudflare dashboard → Zero Trust → Access → Applications → honey-duo.com → Edit policy → Add email

---

## Monitoring

- **Uptime Kuma:** HTTP check on `https://honey-duo.com/api/health`
- **Health endpoint:** `/api/health` — returns `{"status": "ok"}` — no auth required

---

## Security Notes

- `.secrets` is `chmod 600` — only readable by the portal process user
- `.secrets` is in `.gitignore` — never committed
- No session cookies, no passwords stored anywhere in the app
- Direct LAN access without Cloudflare header returns 401
- Unrecognized email (passed Cloudflare but not in `.secrets`) returns 403
- All auth decisions logged to journald