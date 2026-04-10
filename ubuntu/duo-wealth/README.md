# Duo Wealth — Strategy Incubator

**Code Repository:** https://github.com/HoneyDuoDevelopments/Duo-Wealth
**Location:** `/home/honey-duo/Duo-Wealth`
**System:** Ubuntu RTX 3090 (192.168.0.245)
**Status:** 🚧 Phase 1A — Data Foundation

---

## Overview

Algorithmic trading research and deployment platform. Builds, tests, validates, and deploys trading strategies through a structured pipeline: data → backtest → tournament → paper → live.

**This is NOT a trading bot.** It is the workbench that produces and manages trading bots.

---

## Services

### PostgreSQL — Test Instance (Port 5433)
- **Container:** `duo-wealth-db-test`
- **Purpose:** Development and validation database
- **Credentials:** Vaultwarden → Infrastructure → "Duo Wealth DB Test"

### PostgreSQL — Production Instance (Port 5434)
- **Container:** `duo-wealth-db-prod`
- **Purpose:** Production data (started only when ready)
- **Credentials:** Vaultwarden → Infrastructure → "Duo Wealth DB Prod"
- **Profile:** `prod` — must be explicitly started

---

## Service Management

```bash
cd ~/Duo-Wealth/infrastructure

# Test instance (default — always available)
docker compose up -d duo-wealth-db-test
docker compose ps
docker compose logs duo-wealth-db-test -f

# Production instance (explicit start required)
docker compose --profile prod up -d duo-wealth-db-prod

# Connect to test DB
psql -h localhost -p 5433 -U duo_wealth_test -d duo_wealth_test

# Connect to prod DB
psql -h localhost -p 5434 -U duo_wealth -d duo_wealth

# Stop all
docker compose --profile prod down
```

---

## Monitoring Integration

### Uptime Kuma
- **Monitor:** TCP check on `192.168.0.245:5433` (test instance)
- **Interval:** 60 seconds
- **Alert:** Discord on failure

### Prometheus (Future)
- **Exporter:** postgres_exporter on test and prod instances
- **Metrics:** Connection count, query duration, table sizes, replication lag

### Backup
- **Method:** `pg_dump` to OneDrive via rclone
- **Schedule:** Daily (after validation phase)
- **Location:** `OneDrive/Backups/DuoWealth/`

---

## Port Allocation

| Port | Service | Status |
|------|---------|--------|
| 5433 | PostgreSQL Test | 🚧 Phase 1A |
| 5434 | PostgreSQL Prod | 🔜 After validation |

---

## Data Flow

```
External Sources (IBKR, EDGAR, FRD, FRED, OpenFIGI)
    │
    ▼
Ingestion Pipeline (Python)
    │
    ▼
PostgreSQL (operational store — security master, raw prices, 
           corporate actions, pipeline state)
    │
    ▼
Build Pipeline (Python)
    │
    ▼
Parquet Files (research warehouse — adjusted prices, 
              fundamentals, factors)
    │
    ▼
DuckDB (query engine — backtests, research, DataDuo API)
```

---

## Related Documentation

- **Blueprint:** `Duo-Wealth/docs/blueprint.md`
- **Roadmap:** `Duo-Wealth/docs/roadmap.md`
- **Storage ADR:** `Duo-Wealth/docs/adrs/ADR-001-storage-architecture.md`
- **Provider ADR:** `Duo-Wealth/docs/adrs/ADR-002-data-provider-stack.md`

---

## Security Notes

- All database credentials in Vaultwarden — never in code or .env committed to Git
- `.env` file is gitignored
- No external network access to PostgreSQL — localhost only
- IBKR API credentials stored in Vaultwarden separately
- FRD data is personal-use licensed — never served externally

---

**Last Updated:** April 9, 2026
**Phase:** 1A — Data Foundation
