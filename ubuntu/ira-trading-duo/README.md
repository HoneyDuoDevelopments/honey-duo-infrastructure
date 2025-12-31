# IRATradingDuo - Trading Algorithm Infrastructure

**Code Repository:** https://github.com/HoneyDuoDevelopments/ira-trading-duo (FUTURE)  
**Actual Location:** TBD  
**Status:** 🚧 Planned (Future Phase)

---

## Overview

Automated trading algorithms for IRA accounts. High-reliability infrastructure with comprehensive monitoring and alerting.

**Critical Requirements:**
- 99.9% uptime (trading bots must stay operational)
- Real-time alerts on failures
- Secure credential storage
- Audit logging for all trades

---

## Planned Architecture

### Technology Stack
- **Language:** Python (most likely)
- **APIs:** Broker APIs (Interactive Brokers, TD Ameritrade, etc.)
- **Database:** PostgreSQL for trade history
- **Message Queue:** For trade execution

### Deployment
- **Primary:** Ubuntu system (reliable network)
- **Backup:** Cloud deployment (AWS/GCP) for redundancy
- **Failover:** Automated failover to backup if primary down

---

## Integration Points (Future Phase)

### Critical Monitoring
- **Uptime Kuma:** Trading bot health (every 30s)
- **Prometheus:** Trade execution metrics, API latency, balance tracking
- **Grafana:** Dashboard for portfolio performance, bot status
- **Alertmanager:** IMMEDIATE Discord alerts on bot failure

### Logging
- **Loki:** All trade decisions, API calls, errors
- **Audit Log:** Immutable log of all trades (compliance)

### Secrets
- **Vaultwarden:** Broker API keys, credentials
- **Encrypted backups:** Trade history, sensitive data

### Network Access
- **WireGuard VPN:** Remote monitoring and control
- **Web Terminal:** Emergency bot control
- **API Access:** For external integrations

---

## Security Requirements

### Credential Management
- All broker credentials in Vaultwarden
- API keys rotated regularly
- 2FA for all broker accounts
- No secrets in code or logs

### Network Security
- Firewall rules (only necessary outbound connections)
- Rate limiting on API calls
- IP whitelist for broker APIs (if supported)

### Audit Trail
- Every trade logged with timestamp, reason, parameters
- Immutable audit log (write-only)
- Regular backups to OneDrive (encrypted)

---

## Reliability Requirements

### High Availability
- **Primary:** Ubuntu system (wired network)
- **Monitoring:** 30-second health checks
- **Alerts:** Discord notifications for any failures
- **Failover:** Manual or automated to backup instance

### Failure Scenarios
- **Network outage:** Alert immediately, queue trades
- **Bot crash:** Auto-restart via systemd, alert if repeated failures
- **API rate limits:** Backoff and retry logic
- **Account issues:** Alert immediately, halt trading

### Testing
- Paper trading mode for testing strategies
- Backtesting against historical data
- Disaster recovery drills

---

## Deployment (Future)

### Development Workflow
1. Develop and test locally
2. Paper trading on Ubuntu system
3. Gradual rollout to live trading (small positions first)
4. Monitor extensively before scaling

### Service Management
- Systemd service with auto-restart
- Health check endpoint
- Graceful shutdown (close positions before stopping)

---

## Compliance Considerations

### Record Keeping
- All trades logged (required for tax reporting)
- API call logs (for broker audit)
- Performance tracking (for strategy evaluation)

### Tax Reporting
- Export trade history for tax software
- Track cost basis, wash sales
- Generate tax documents

---

## Development Roadmap

**Phase 1:**
1. Infrastructure setup (monitoring, logging)
2. Basic bot framework
3. Paper trading integration
4. Alert system testing

**Phase 2:**
1. Live trading with small positions
2. Performance tracking
3. Strategy optimization
4. Failover testing

**Phase 3:**
1. Advanced strategies
2. Multi-account support
3. Cloud backup deployment
4. Automated failover

---

## Related Projects

- **Infrastructure:** Monitoring, secrets, VPN (THIS PROJECT - Phase 0)
- **Future:** Dashboard for portfolio visualization

---

## Notes

This is a **high-stakes** project requiring:
- Extensive testing
- Comprehensive monitoring
- Fail-safe mechanisms
- Regular audits

Do NOT rush deployment. Test thoroughly.
