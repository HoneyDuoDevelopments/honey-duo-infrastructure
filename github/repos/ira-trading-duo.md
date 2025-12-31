# IRATradingDuo Repository Reference

**Quick access for Claude integration**

## Repository Info
- **URL:** https://github.com/HoneyDuoDevelopments/ira-trading-duo
- **Local Path:** `/home/honey-duo/ira-trading-duo`
- **System:** Ubuntu
- **Status:** Future phase (pending)

## Purpose
⚠️ **CRITICAL SYSTEM:** Automated trading for IRA accounts.

## Technology Stack (Planned)
- Python
- Broker APIs (Interactive Brokers, TD Ameritrade)
- PostgreSQL (trade history, audit logs)
- Redis/RabbitMQ (trade execution queue)

## Security Requirements
- All credentials in Vaultwarden
- Comprehensive audit logging
- Immutable trade records
- No secrets in code or Git

## Integration Points
- Monitoring: `~/honey-duo-infrastructure/ubuntu/ira-trading-duo/integration/`
- Deployment: `~/honey-duo-infrastructure/ubuntu/ira-trading-duo/deployment/`
- Docs: `~/honey-duo-infrastructure/ubuntu/ira-trading-duo/README.md`

## Critical Monitoring
- 30-second health checks (Uptime Kuma)
- Immediate Discord alerts on failure
- Prometheus metrics (trades, latency, balance)
- Complete audit log to Loki

## When Sharing with Claude
⚠️ **NEVER share:**
- Actual API keys or credentials
- Real account numbers
- Actual trade data (use examples)

✅ **Safe to share:**
- Algorithm logic
- Strategy code
- Test data
- Integration code
- Monitoring configs

**Process:**
1. Sanitize code (remove all credentials)
2. Push to GitHub
3. Share repo URL with Claude
4. Claude can review logic, security, testing
