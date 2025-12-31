# DesignDuo Repository Reference

**Quick access for Claude integration**

## Repository Info
- **URL:** https://github.com/HoneyDuoDevelopments/design-duo
- **Local Path:** `/home/honey-duo/design-duo`
- **System:** Ubuntu RTX 3090
- **Status:** Phase 1 (pending)

## Purpose
ComfyUI-based AI image generation service for Sticker Duo platform.

## Technology Stack (Planned)
- ComfyUI (Stable Diffusion interface)
- Python API wrapper (FastAPI)
- SDXL models + LoRAs
- Redis queue for batch processing

## Integration Points
- Monitoring: `~/honey-duo-infrastructure/ubuntu/design-duo/integration/`
- Deployment: `~/honey-duo-infrastructure/ubuntu/design-duo/deployment/`
- Docs: `~/honey-duo-infrastructure/ubuntu/design-duo/README.md`

## GPU Requirements
- RTX 3090 (24GB VRAM)
- ~16GB system RAM
- ~50GB storage for models

## When Sharing with Claude
- Push code to GitHub first
- Share repo URL: https://github.com/HoneyDuoDevelopments/design-duo
- Reference specific files or commits
- Claude can review structure, suggest improvements, help debug
