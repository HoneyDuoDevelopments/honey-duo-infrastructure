# code-server - VSCode in Browser

**URL:** https://code.honey-duo.com  
**Port:** 8443  
**Status:** ✅ Running  
**Purpose:** Full VSCode development environment accessible from any browser

---

## Overview

Browser-based Visual Studio Code for remote development work. Provides complete IDE functionality with extensions, integrated terminal, Git integration, and file management.

**Primary Use Case:** Development from Tesla work laptop (corporate network blocks VPN/SSH)

---

## Access

### From Any Browser (Tesla Laptop, Phone, Home)

1. Navigate to https://code.honey-duo.com
2. **Cloudflare Access 2FA:**
   - Enter email address
   - Click "Send me a code"
   - Check email for 6-digit code
   - Enter code (expires in 10 minutes)
3. **code-server Password:**
   - Get from Vaultwarden → Infrastructure → "code-server"
   - Enter password
4. ✅ Full VSCode interface loads

### Security Layers
```
User Browser
    ↓ HTTPS (443)
Cloudflare (SSL, DDoS protection)
    ↓
Cloudflare Access (2FA via Email OTP)
    ├─ Allowed: your-email@gmail.com, wife-email@gmail.com
    ├─ Session: 1 hour timeout
    └─ Geographic: United States only
    ↓
Cloudflare Tunnel (encrypted, zero trust)
    ↓
code-server Password (64-char random)
    ↓
File System Permissions (honey-duo user)
    ↓
VSCode Running on Ubuntu
```

---

## Features

### Full VSCode Functionality
- Syntax highlighting for all languages
- IntelliSense and auto-completion
- Integrated terminal (bash)
- Git integration (commit, push, pull)
- Extensions marketplace
- Multi-file editing with tabs
- Split panes
- Search and replace across files
- Debugging support

### Workspace Access
- **Root:** `/home/coder/workspace` → `/home/honey-duo`
- **Infrastructure Repo:** `/home/coder/workspace/honey-duo-infrastructure`
- **All Projects:** Full access to home directory
- **Docker:** Can manage containers via terminal

### Installed Extensions (Optional)
```bash
# Install extensions via terminal in code-server
code-server --install-extension ms-python.python
code-server --install-extension ms-azuretools.vscode-docker
code-server --install-extension redhat.vscode-yaml
```

---

## Service Management
```bash
cd ~/honey-duo-infrastructure/ubuntu/code-server

# Check status
docker compose ps

# View logs
docker compose logs -f

# Restart
docker compose restart

# Stop
docker compose down

# Start
docker compose up -d

# Update to latest version
docker compose pull
docker compose up -d
```

---

## Configuration

### Docker Compose
- **Image:** codercom/code-server:latest
- **Port:** 8443 → 8080 (internal)
- **User:** 1000:1000 (honey-duo)
- **Workspace:** /home/honey-duo mounted as /home/coder/workspace

### Environment Variables (.env - gitignored)
```bash
CODE_SERVER_PASSWORD=<64-char-random>  # Stored in Vaultwarden
```

### Cloudflare Tunnel
```yaml
# /etc/cloudflared/config.yml
- hostname: code.honey-duo.com
  service: http://localhost:8443
```

---

## Common Tasks

### Editing Infrastructure Code
1. Open https://code.honey-duo.com
2. Navigate to `workspace/honey-duo-infrastructure`
3. Edit files
4. Use integrated terminal for Git commands:
```bash
cd honey-duo-infrastructure
git status
git add .
git commit -m "Your changes"
git push origin main
```

### Running Python Scripts
1. Create/edit Python file
2. Open integrated terminal (Ctrl+`)
3. Run script:
```bash
python3 your_script.py
```

### Managing Docker Containers
```bash
# In integrated terminal
docker ps
docker compose -f ~/honey-duo-infrastructure/ubuntu/monitoring/docker-compose.yml restart grafana
```

### Installing Python Packages
```bash
# In integrated terminal
pip install --break-system-packages package-name
```

---

## Security Notes

### What code-server CAN Access
- ✅ All files in /home/honey-duo
- ✅ Infrastructure repository
- ✅ Docker commands (manage containers)
- ✅ Git operations
- ✅ Read system logs
- ⚠️ Modify infrastructure configs (with caution)

### What code-server CANNOT Access (without sudo)
- ❌ Root-owned files
- ❌ System service management (needs sudo)
- ❌ System package installation (needs sudo)
- ❌ Firewall modifications (needs sudo)

### Audit Trail
- **Cloudflare Access Logs:** All authentication attempts
- **code-server Logs:** All access and file operations
- **System Logs:** All sudo commands
- **Git History:** All code changes

### Emergency Revocation
If compromised:
1. Disable Cloudflare Access policy (instant cutoff)
2. Change code-server password (in .env)
3. Restart container: `docker compose restart`
4. Review logs for suspicious activity

---

## Troubleshooting

### Cannot Access from Browser
```bash
# Check container status
docker compose ps

# Should show "Up" status
# If not:
docker compose logs code-server

# Check Cloudflare tunnel
sudo systemctl status cloudflared

# Test local access
curl -I http://localhost:8443
```

### 2FA Not Sending Email
- Check spam folder
- Code expires in 10 minutes
- Verify email in Cloudflare Access policy
- Check you're in United States (geographic restriction)

### Password Not Working
- Get correct password from Vaultwarden
- Copy-paste to avoid typos
- Check .env file has correct password:
```bash
cat ~/honey-duo-infrastructure/ubuntu/code-server/.env
```

### Extensions Not Working
- Some extensions require specific dependencies
- Install via integrated terminal:
```bash
code-server --install-extension extension-id
```

### Slow Performance
- code-server runs on Ubuntu (good specs)
- Network latency depends on connection
- Close unused tabs/files
- Restart container if memory high

---

## Monitoring Integration

### Uptime Kuma (After Phase 0 Complete)
- **Monitor:** HTTP check on https://code.honey-duo.com
- **Alert:** Discord on downtime

### Prometheus Metrics
- Container health via Docker metrics
- Response time monitoring

### Grafana Dashboard
- Service uptime
- Resource usage (CPU, memory)

---

## Resource Usage

**Typical:**
- CPU: 5-10% idle, 20-40% when editing
- Memory: ~200-300MB
- Disk: ~500MB (image + config)

**Network:**
- Minimal when idle
- Depends on file operations and terminal commands

---

## Comparison: code-server vs Alternatives

| Feature | code-server | VPN + SSH | Local VSCode + Remote SSH |
|---------|-------------|-----------|---------------------------|
| Works from Tesla | ✅ Yes | ❌ Blocked | ❌ Blocked |
| No install needed | ✅ Yes | ❌ Needs VPN client | ❌ Needs VSCode |
| Full IDE | ✅ Yes | ❌ Terminal only | ✅ Yes |
| Admin rights needed | ❌ No | ✅ Yes (VPN) | ❌ No |
| Works on phone | ✅ Yes | ⚠️ Terminal apps | ❌ No |
| Security | 🟡 Very Good | 🟢 Best | 🟢 Best |

---

## Future Enhancements

- [ ] Add recommended extensions to Dockerfile
- [ ] Configure settings.json for consistent environment
- [ ] Add snippets for common tasks
- [ ] Create dashboard for quick access to projects
- [ ] Integrate with Grafana for code change metrics

---

**Last Updated:** January 7, 2026  
**Component:** Phase 0 - Component 4 Extension  
**Next:** Component 5 - Loki & Promtail Logging
