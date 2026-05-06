# Windows 1070 — Emulation & Streaming Node

**Hostname:** DESKTOP-UCI3214  
**IP Address:** 192.168.0.137 (Static — Reserved via TP-Link Archer DHCP reservation)  
**OS:** Windows 10 Pro 22H2 (Build 19045)  
**Role:** Emulation host + Moonlight/Sunshine streaming server  
**Status:** ✅ Operational (May 2026)

> ⚠️ This node has NO infrastructure repo clone. It is a dedicated emulation/streaming box only.  
> All management is done via SSH from Pi or directly on the machine.

---

## Hardware

| Component | Details |
|-----------|---------|
| **CPU** | Intel Core i5-3550 @ 3.30GHz (4c/4t, Ivy Bridge 2012, LGA1155) |
| **RAM** | 16GB DDR3 @ 1600MHz (4x4GB Micron — all slots populated) |
| **GPU** | NVIDIA GeForce GTX 1070 8GB (Driver: 32.0.15.6094) |
| **Storage 1** | Samsung SSD 860 EVO 500GB — OS Drive |
| **Storage 2** | SK Hynix SC311 SATA 128GB — Secondary |
| **Network** | Intel Wi-Fi AC 7265 + Intel 82579LM Gigabit Ethernet (wired) |

---

## Network

| Property | Value |
|----------|-------|
| **Local IP** | 192.168.0.137 |
| **Assignment** | Static via TP-Link Archer DHCP reservation |
| **Connection** | Wired Ethernet (required for streaming performance) |
| **Sunshine Port** | 47990 (web UI + pairing) |

---

## Installed Software

| App | Version | Location | Install Method |
|-----|---------|----------|----------------|
| Sunshine | 2025.924 | `C:\Program Files\Sunshine\` | winget |
| PCSX2 | 2.6.3 | `C:\Program Files\PCSX2\` | winget |
| Dolphin | 2603a (Mar 2026) | `C:\HoneyDuo\gaming\emulators\dolphin\` | Manual portable |
| RetroArch | 1.22.2 | `C:\RetroArch-Win64\` | winget |
| 7-Zip | 26.01 | `C:\Program Files\7-Zip\` | winget |
| Python | 3.12.10 | AppData | winget |

### RetroArch Cores Installed
| Core | File | Platform |
|------|------|----------|
| Beetle PSX | `mednafen_psx_libretro.dll` | PS1 |
| Mupen64Plus-Next | `mupen64plus_next_libretro.dll` | N64 |

---

## Folder Structure

```
C:\HoneyDuo\
└── gaming\
    ├── emulators\
    │   └── dolphin\              ← Dolphin portable (v2603a)
    ├── roms\
    │   ├── ps1\                  ← PS1 ROMs (.bin/.cue)
    │   ├── ps2\                  ← PS2 ROMs (.iso)
    │   ├── n64\                  ← N64 ROMs (.z64/.n64)
    │   ├── gamecube\             ← GameCube ROMs (.iso/.gcm)
    │   └── wii\                  ← Wii ROMs
    ├── bios\
    │   ├── ps1\                  ← PS1 BIOS source copies
    │   └── ps2\                  ← PS2 + PS1 BIOS (69 files total)
    ├── saves\
    │   ├── pcsx2\savestates\
    │   ├── pcsx2\memcards\
    │   └── retroarch\states\
    ├── screenshots\
    └── configs\
        └── pcsx2\
```

> **Future:** When ROMs migrate to 3070 Ti node, only update ROM paths in emulator configs.  
> Everything else stays the same.

---

## Emulator Configuration

### PCSX2 — PS2 Only
- **Config:** `C:\Users\samue\Documents\PCSX2\inis\PCSX2.ini`
- **BIOS:** `C:\HoneyDuo\gaming\bios\ps2\` (ps2-0230a-20080220.bin active)
- **ROMs:** `C:\HoneyDuo\gaming\roms\ps2\` only
- **Renderer:** Direct3D 11 ⚠️ (Vulkan causes crashes on this hardware)
- **IMPORTANT:** PS1 games go through RetroArch, NOT PCSX2

### RetroArch — PS1 + N64
- **Config:** `C:\RetroArch-Win64\retroarch.cfg`
- **ROMs:** `C:\HoneyDuo\gaming\roms\`
- **BIOS:** `C:\HoneyDuo\gaming\bios\`
- **PS1 Launch:** `retroarch.exe -L mednafen_psx_libretro.dll <rom.cue>`
- **N64 Launch:** `retroarch.exe -L mupen64plus_next_libretro.dll <rom.z64>`

### Dolphin — GameCube + Wii
- **Config:** `C:\Users\samue\AppData\Roaming\Dolphin Emulator\Config\Dolphin.ini`
- **ROMs:** `C:\HoneyDuo\gaming\roms\gamecube\` + `roms\wii\`
- **Backend:** Direct3D 11

---

## Sunshine Streaming

- **Web UI:** https://localhost:47990
- **Encoder:** NVENC (GTX 1070 hardware encoder)
- **Paired Clients:** HoneyDuo-Pi (192.168.0.193)

### Registered Applications
| Name | Command |
|------|---------|
| RetroArch | `C:\RetroArch-Win64\retroarch.exe` |
| PCSX2 | `C:\Program Files\PCSX2\pcsx2-qt.exe` |
| Dolphin | `C:\HoneyDuo\gaming\emulators\dolphin\Dolphin.exe` |
| Steam | `C:\Program Files (x86)\Steam\steam.exe` |

### Optimized Stream Settings
| Setting | Value |
|---------|-------|
| Encoder | nvenc |
| NVENC Preset | p1 (lowest latency) |
| Two-pass | Off |
| Client Codec | H.264 (Pi cannot decode H.265) |
| Bitrate | 15-20 Mbps |
| Resolution | 1080p @ 60fps |

---

## Moonlight Clients

| Client | Device | Connection | Notes |
|--------|--------|------------|-------|
| Pi 5 | honeyduo-pi58gb | Wi-Fi | Launch: `DISPLAY=:0 flatpak run com.moonlight_stream.Moonlight` |
| Fire TV | Bedroom TV | Wi-Fi | Moonlight app from Fire TV store |

**Exit hotkey:** `Ctrl + Alt + Shift + Q`  
**Fullscreen toggle:** `Ctrl + Alt + Shift + F`

---

## Windows Optimizations Applied

- High Performance power plan enabled
- Game Mode enabled
- Nagle's Algorithm disabled (all network interfaces)
- SystemResponsiveness = 10
- Gaming task priority = High
- Xbox Game Bar disabled
- NVIDIA Control Panel: Power = Max Performance, Shader Cache = 10GB

---

## BIOS Inventory

**Location:** `C:\HoneyDuo\gaming\bios\ps2\` (69 files)

| Region | Files |
|--------|-------|
| NTSC-UC (USA) | ps-20a through psone-45a |
| NTSC-J (Japan) | ps-10j through psone-43j |
| PAL-E (Europe) | ps-20e through psone-45e |
| PS2 Full Set | ps2-0100j (2000) through ps2-0230e (2008) |

---

## Infrastructure Integration

| Service | Status | Notes |
|---------|--------|-------|
| Uptime Kuma | ⏳ TODO | Add HTTP monitor on port 47990 |
| Grafana | ❌ Not planned | Emulation box only |
| Vaultwarden | ✅ Use existing | Store Sunshine credentials |
| Portal | ⏳ TODO | Add gaming node to portal dashboard |

---

## Future Tasks

- [ ] Add Sunshine (port 47990) to Uptime Kuma monitoring
- [ ] Migrate ROM library to 3070 Ti node (network share)
- [ ] Set up 3070 Ti as primary Sunshine host
- [ ] Add node to Portal dashboard
- [ ] Update NVIDIA drivers
- [ ] Test additional Moonlight clients (phones, tablets)
- [ ] Add GameCube ROM test

---

## Key Lessons / Gotchas

- **Vulkan crashes PCSX2** on this hardware — always use Direct3D 11
- **PCSX2 config lives in Documents**, not AppData — overwrites on first launch
- **PS1 BIOS must be in the PS2 BIOS folder** for PCSX2 to find it
- **PS1 games use RetroArch** (Beetle PSX core), NOT PCSX2
- **H.265 causes ghosting on Pi** — always stream H.264 to Pi clients
- **NoMachine conflicts with Pi HDMI** — run `sudo systemctl restart display-manager` to restore
- **Moonlight on Pi requires** `DISPLAY=:0` prefix when launching via SSH
- **Dolphin is portable** — lives in HoneyDuo folder, not Program Files

---

**Last Updated:** May 4, 2026  
**Setup By:** Sam + Claude  
**Session:** Initial 1070 node setup, emulation stack, Sunshine/Moonlight integration