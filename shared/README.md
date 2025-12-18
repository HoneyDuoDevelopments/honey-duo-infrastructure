# Shared Resources

Common scripts, configurations, and documentation used across both systems.

## Scripts

Scripts that work on both Pi and Ubuntu:

- `install-docker.sh` - Docker installation script
- `setup-monitoring-agent.sh` - Install Node Exporter + Promtail
- `common-functions.sh` - Bash functions library
- `backup-configs.sh` - Backup all configs to OneDrive

## Configs

Template configurations:

- `.env.template` - Environment variable template
- `docker-compose.template` - Docker compose template
- `systemd-service.template` - Systemd service template

## Documentation

Cross-system documentation:

- `common-patterns.md` - Design patterns and best practices
- `docker-patterns.md` - Docker deployment patterns
- `security-patterns.md` - Security best practices
