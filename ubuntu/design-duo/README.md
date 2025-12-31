# DesignDuo - AI Image Generation for Sticker Duo

**Code Repository:** https://github.com/HoneyDuoDevelopments/design-duo (FUTURE)  
**Actual Location:** TBD  
**Status:** 🚧 Planned (Phase 1)

---

## Overview

ComfyUI-based AI image generation service for creating sticker designs. Utilizes RTX 3090 GPU for high-quality image generation.

**Purpose:** Generate unique sticker designs for Sticker Duo e-commerce platform

---

## Planned Architecture

### Hardware Requirements
- **GPU:** RTX 3090 (24GB VRAM)
- **RAM:** 16GB minimum
- **Storage:** ~50GB for models

### Technology Stack
- **ComfyUI:** Web-based stable diffusion interface
- **Backend:** Python API wrapper (FastAPI or Flask)
- **Models:** Stable Diffusion XL, LoRAs for sticker styles
- **Queue System:** For batch processing

---

## Integration Points (Phase 1)

### Monitoring
- **Uptime Kuma:** HTTP health checks
- **Prometheus:** GPU metrics, generation queue length, processing time
- **Grafana:** Dashboard for GPU utilization, queue status

### Logging
- **Loki:** Application logs, error tracking
- **Promtail:** Log shipping configuration

### Secrets
- **Vaultwarden:** API keys, service credentials

### Access
- **External:** Via Cloudflare tunnel (for Sticker Duo integration)
- **Internal:** Direct access for development

---

## Deployment (Future)

### Service Management
Service will run as systemd service or Docker container.

**Planned location:** `/home/honey-duo/design-duo/` OR in Docker

### Resource Allocation
- **GPU:** Dedicated RTX 3090
- **RAM:** 16GB allocated
- **CPU:** 4-8 cores

---

## Development Roadmap

**Phase 1 (Post-Infrastructure):**
1. ComfyUI installation and GPU optimization
2. API wrapper development
3. Model selection and testing
4. Integration with monitoring stack
5. Cloudflare tunnel setup

**Phase 2:**
1. Sticker Duo integration
2. Batch processing queue
3. Cost tracking (GPU time)
4. Automated model updates

---

## Related Projects

- **Sticker Duo:** E-commerce platform (will consume DesignDuo API)
- **Infrastructure:** Monitoring, secrets, VPN access

---

## Notes

This is a **placeholder** for Phase 1 development. Structure and deployment details will be finalized during implementation.
