# Vaultwarden CLI Guide - Scripts & Automation

How to retrieve secrets programmatically for scripts, bots, and automation.

## Quick Reference

```bash
# One-liner to get a password
BW_SESSION=$(bw unlock --raw) && bw get password "Item Name"
```

## Setup (Already Done)

CLI is installed on both systems:
- **Pi:** `/usr/local/bin/bw` (via npm)
- **Ubuntu:** `/usr/local/bin/bw` (binary)

Server configured: `https://vault.honey-duo.com`

## Authentication Methods

### Method 1: Interactive (Manual Use)

```bash
# Login (one-time, stores session)
bw login

# Unlock vault (needed each session)
export BW_SESSION=$(bw unlock --raw)

# Now use commands
bw get password "Cloudflare"
```

### Method 2: Environment Variables (Scripts)

```bash
# Set these in your script or environment
export BW_CLIENTID="user.your-client-id"
export BW_CLIENTSECRET="your-client-secret"
export BW_PASSWORD="your-master-password"

# Then in script:
bw login --apikey
export BW_SESSION=$(bw unlock --raw)
bw get password "Item Name"
```

**To get API key:**
1. Web vault → Settings → Security → Keys
2. View API Key
3. Store Client ID and Client Secret in secure location

### Method 3: Session File (Persistent Scripts)

```bash
# Save session to file (careful - this is sensitive!)
bw unlock --raw > ~/.bw_session
chmod 600 ~/.bw_session

# In scripts:
export BW_SESSION=$(cat ~/.bw_session)
bw get password "Item Name"

# Session expires after timeout - need to refresh
```

## Common Commands

### Get Password
```bash
bw get password "Item Name"
bw get password "Cloudflare"
```

### Get Username
```bash
bw get username "Item Name"
```

### Get Full Item (JSON)
```bash
bw get item "Item Name"
bw get item "Item Name" | jq '.login.password'
```

### Get Secure Note
```bash
bw get notes "Vaultwarden Admin Token"
```

### Get Custom Field
```bash
bw get item "Item Name" | jq -r '.fields[] | select(.name=="API_KEY") | .value'
```

### Search Items
```bash
bw list items --search "cloudflare"
```

### List by Collection
```bash
# Get collection ID first
bw list collections

# List items in collection
bw list items --collectionid "f8e5b16b-4a50-400f-9e6f-46f40bb9c960"
```

## Script Examples

### Example 1: Simple Password Retrieval

```bash
#!/bin/bash
# get-password.sh

ITEM_NAME="$1"

if [ -z "$BW_SESSION" ]; then
    export BW_SESSION=$(bw unlock --raw)
fi

bw get password "$ITEM_NAME"
```

Usage: `./get-password.sh "Cloudflare"`

### Example 2: Script with Error Handling

```bash
#!/bin/bash
# secure-script.sh

set -e

# Ensure vault is unlocked
if [ -z "$BW_SESSION" ]; then
    echo "Unlocking vault..."
    export BW_SESSION=$(bw unlock --raw)
fi

# Sync to get latest
bw sync

# Get credentials
DB_PASSWORD=$(bw get password "Database Production")
API_KEY=$(bw get notes "API Key - Service X")

if [ -z "$DB_PASSWORD" ] || [ -z "$API_KEY" ]; then
    echo "ERROR: Failed to retrieve credentials"
    exit 1
fi

# Use credentials...
echo "Credentials loaded successfully"
```

### Example 3: Python Integration

```python
#!/usr/bin/env python3
import subprocess
import os
import json

def get_bw_session():
    """Get or create Bitwarden session"""
    session = os.environ.get('BW_SESSION')
    if not session:
        result = subprocess.run(
            ['bw', 'unlock', '--raw'],
            capture_output=True,
            text=True,
            input=os.environ.get('BW_PASSWORD', '')
        )
        session = result.stdout.strip()
        os.environ['BW_SESSION'] = session
    return session

def get_password(item_name):
    """Get password from Vaultwarden"""
    session = get_bw_session()
    result = subprocess.run(
        ['bw', 'get', 'password', item_name, '--session', session],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def get_item(item_name):
    """Get full item as dict"""
    session = get_bw_session()
    result = subprocess.run(
        ['bw', 'get', 'item', item_name, '--session', session],
        capture_output=True,
        text=True
    )
    return json.loads(result.stdout)

# Usage
if __name__ == "__main__":
    password = get_password("Cloudflare")
    print(f"Retrieved password: {password[:3]}...")
```

### Example 4: Systemd Service with Secrets

```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=myuser
Environment="BW_SESSION=<session-token>"
ExecStartPre=/bin/bash -c 'export API_KEY=$(/usr/local/bin/bw get password "My API Key" --session $BW_SESSION)'
ExecStart=/usr/local/bin/myapp
Restart=always

[Install]
WantedBy=multi-user.target
```

## Best Practices

### DO:
- ✅ Use API keys for automated scripts
- ✅ Store session tokens with `chmod 600`
- ✅ Use `--session` flag instead of env var when possible
- ✅ Sync before retrieving (`bw sync`)
- ✅ Handle errors gracefully

### DON'T:
- ❌ Hardcode master password in scripts
- ❌ Commit session tokens to Git
- ❌ Log passwords to stdout/files
- ❌ Share session tokens between users
- ❌ Leave sessions unlocked indefinitely

## Troubleshooting

### "Vault is locked"
```bash
export BW_SESSION=$(bw unlock --raw)
```

### "You are not logged in"
```bash
bw login
```

### "Session expired"
```bash
# Re-unlock
export BW_SESSION=$(bw unlock --raw)
```

### "Item not found"
```bash
# Check exact name
bw list items --search "partial name"

# Use ID instead
bw get item "c5c27fad-a2f9-493c-9a2e-1f6989a0ec77"
```

### Sync issues
```bash
bw sync --force
```

## Security Notes

1. **Session tokens** are equivalent to being logged in - protect them
2. **API keys** should be stored securely (ironically, in Vaultwarden itself or env vars)
3. **Master password** in environment variables is a risk - use API keys for automation
4. **Timeout**: Sessions expire based on vault settings - scripts should handle re-auth

## Integration with Infrastructure

For Honey Duo infrastructure, secrets are stored in the **Infrastructure** collection:

| Item Name | Contains |
|-----------|----------|
| Vaultwarden Admin Token | Admin panel access |
| Vaultwarden Backup Password | Backup encryption key |
| Pi-hole Admin | Pi-hole password |
| HoneyDuo Gaming App | Gaming app password |
| Router Admin | Router credentials |
| Cloudflare | Cloudflare login |

Retrieve for scripts:
```bash
# Example: Get Pi-hole password for automation
PIHOLE_PASS=$(bw get password "Pi-hole Admin")
```