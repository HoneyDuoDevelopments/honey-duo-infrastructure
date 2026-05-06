# HoneyDuo Gaming Infrastructure — Node Documentation
**Created:** May 4, 2026  
**Session:** 1070 Gaming Node Setup & Sunshine Streaming Integration

---

## 📡 Network Infrastructure

### Subnet: 192.168.0.x

| Device | Hostname | IP Address | Connection | Role |
|--------|----------|------------|------------|------|
| Raspberry Pi 5 | honeyduo-pi58gb | 192.168.0.193 | Wi-Fi | Always-on services + Moonlight client |
| Ubuntu RTX 3090 | honeyduo (Ubuntu) | 192.168.0.245 | Wired | Heavy compute node |
| Windows GTX 1070 | DESKTOP-UCI3214 | 192.168.0.137 | Wired (was Wi-Fi) | Emulation + Sunshine streaming host |

### Cloudflare / External
- Domain: **honey-duo.com**
- Cloudflare tunnels in use for remote access to Pi services

### Speed Test Results (1070 Node)
- Wi-Fi: ~500 Mbps down / 90 Mbps up
- Wired (Ethernet): ~900 Mbps down / 90 Mbps up
- **Recommendation: Always keep 1070 node wired for best streaming performance**

---

## 🖥️ 1070 Node — Hardware Specs

| Component | Details |
|-----------|---------|
| **Hostname** | DESKTOP-UCI3214 |
| **OS** | Windows 10 Pro 22H2 (Build 19045) |
| **CPU** | Intel Core i5-3550 @ 3.30GHz (4 cores / 4 threads, Ivy Bridge 2012) |
| **RAM** | 16GB DDR3 @ 1600MHz (4x4GB Micron, all DIMM slots populated) |
| **GPU** | NVIDIA GeForce GTX 1070 8GB (Driver: 32.0.15.6094) |
| **Storage 1** | Samsung SSD 860 EVO 500GB — OS Drive — Healthy |
| **Storage 2** | SK Hynix SC311 SATA 128GB — Secondary SSD — Healthy |
| **Network** | Intel Wi-Fi AC 7265 + Intel 82579LM Gigabit Ethernet |
| **Local IP** | 192.168.0.137 (Wi-Fi) |

### CPU Bottleneck Notes
- i5-3550 is LGA1155 socket — dead platform, no upgrade path on this board
- Bottleneck is real but acceptable for this node's intended use case
- Not suitable for modern AAA gaming but excellent for emulation + Moonlight hosting

---

## 📁 HoneyDuo Folder Structure

```
C:\HoneyDuo\
└── gaming\
    ├── emulators\
    │   └── dolphin\              ← Dolphin portable install (v2603a)
    ├── roms\
    │   ├── ps1\                  ← PS1 ROMs (.bin/.cue format)
    │   ├── ps2\                  ← PS2 ROMs (.iso format)
    │   ├── n64\                  ← N64 ROMs (.z64/.n64)
    │   ├── gamecube\             ← GameCube ROMs (.iso/.gcm)
    │   └── wii\                  ← Wii ROMs
    ├── bios\
    │   ├── ps1\                  ← PS1 BIOS files (SCPH series)
    │   └── ps2\                  ← PS2 BIOS files (69 files, full set)
    │                               ← PS1 BIOS also copied here for PCSX2
    ├── saves\
    │   ├── pcsx2\
    │   │   ├── savestates\
    │   │   └── memcards\
    │   └── retroarch\
    │       └── states\
    ├── screenshots\
    └── configs\
        └── pcsx2\
            ├── logs\
            ├── cheats\
            └── patches\
```

---

## 🎮 Installed Software

### Emulators

| App | Version | Install Location | Install Method |
|-----|---------|-----------------|----------------|
| **PCSX2** | 2.6.3 | `C:\Program Files\PCSX2\` | winget |
| **Dolphin** | 2603a (2026) | `C:\HoneyDuo\gaming\emulators\dolphin\` | Manual portable |
| **RetroArch** | 1.22.2 | `C:\RetroArch-Win64\` | winget |
| **Sunshine** | 2025.924.154138 | `C:\Program Files\Sunshine\` | winget |
| **7-Zip** | 26.01 | `C:\Program Files\7-Zip\` | winget |
| **Python** | 3.12.10 | `C:\Users\samue\AppData\Local\Programs\Python\Python312\` | winget |

### Winget IDs (for reinstall reference)
```powershell
winget install -e --id PCSX2Team.PCSX2
winget install -e --id DolphinEmulator.Dolphin   # Old 5.0 — use manual portable instead
winget install -e --id Libretro.RetroArch
winget install -e --id LizardByte.Sunshine
winget install -e --id 7zip.7zip
winget install -e --id Python.Python.3.12
```

---

## 🕹️ Emulator Configuration

### PCSX2 (PS2 Only)
- **Config Location:** `C:\Users\samue\Documents\PCSX2\inis\PCSX2.ini`
- **BIOS Folder:** `C:\HoneyDuo\gaming\bios\ps2\` (contains both PS1 and PS2 BIOS)
- **ROM Path:** `C:\HoneyDuo\gaming\roms\ps2\`
- **Renderer:** Direct3D 11 (NOT Vulkan — causes crashes on this hardware)
- **BIOS Selected:** `ps2-0230a-20080220.bin` (latest USA PS2 BIOS)
- **IMPORTANT:** PCSX2 is configured for **PS2 only** — do not add PS1 ROM paths

#### PCSX2 Performance Settings
| Setting | Value |
|---------|-------|
| Renderer | Direct3D 11 |
| Internal Resolution | 2x Native |
| EE Cycle Rate | -1 |
| MTVU | Enabled |
| Fast Boot | Enabled |

### RetroArch (PS1 + N64)
- **Config Location:** `C:\RetroArch-Win64\retroarch.cfg`
- **ROM Browser Root:** `C:\HoneyDuo\gaming\roms\`
- **BIOS/System Folder:** `C:\HoneyDuo\gaming\bios\`
- **Save Location:** `C:\HoneyDuo\gaming\saves\retroarch\`
- **Video Driver:** Vulkan
- **Audio Driver:** WASAPI

#### Installed Cores
| Core | File | Platform |
|------|------|----------|
| Beetle PSX | `mednafen_psx_libretro.dll` | PS1 |
| Mupen64Plus-Next | `mupen64plus_next_libretro.dll` | N64 |

#### RetroArch Launch Commands
```powershell
# PS1
Start-Process "C:\RetroArch-Win64\retroarch.exe" -ArgumentList "-L `"C:\RetroArch-Win64\cores\mednafen_psx_libretro.dll`" `"PATH_TO_ROM.cue`""

# N64
Start-Process "C:\RetroArch-Win64\retroarch.exe" -ArgumentList "-L `"C:\RetroArch-Win64\cores\mupen64plus_next_libretro.dll`" `"PATH_TO_ROM.z64`""
```

#### RetroArch Performance Settings
| Setting | Value |
|---------|-------|
| Hard GPU Sync | On |
| Max Swapchain Images | 2 |
| Frame Delay | 3 |

### Dolphin (GameCube / Wii)
- **Config Location:** `C:\Users\samue\AppData\Roaming\Dolphin Emulator\Config\Dolphin.ini`
- **ROM Paths:** `C:\HoneyDuo\gaming\roms\gamecube\` and `C:\HoneyDuo\gaming\roms\wii\`
- **Version:** 2603a (March 2026 dev build) — portable, no installer

#### Dolphin Performance Settings
| Setting | Value |
|---------|-------|
| CPU Emulator Engine | JIT Recompiler |
| Dual Core | Enabled |
| Internal Resolution | 2x Native |
| Backend | Direct3D 11 |

---

## 🌞 Sunshine Configuration

- **Web UI:** https://localhost:47990
- **Service:** Runs as Windows service (auto-start)
- **Encoder:** NVENC (GTX 1070 hardware encoder)
- **Paired Clients:** HoneyDuo-Pi (Raspberry Pi 5)

### Sunshine Applications
| App Name | Command |
|----------|---------|
| RetroArch | `C:\RetroArch-Win64\retroarch.exe` |
| PCSX2 | `C:\Program Files\PCSX2\pcsx2-qt.exe` |
| Dolphin | `C:\HoneyDuo\gaming\emulators\dolphin\Dolphin.exe` |
| Steam | `C:\Program Files (x86)\Steam\steam.exe` |

### Sunshine Advanced Settings (Optimized)
| Setting | Value |
|---------|-------|
| Encoder | nvenc |
| NVENC Preset | p1 (lowest latency) |
| Two-pass mode | Off |
| VBV Percentage | 150 |

---

## 📺 Moonlight Clients

### Raspberry Pi 5 (Primary Client)
- **Install Method:** Flatpak
- **Launch Command:** `DISPLAY=:0 flatpak run com.moonlight_stream.Moonlight`
- **Version:** 6.1.0
- **Host Added:** 192.168.0.137 (1070 node)
- **Exit Hotkey:** `Ctrl + Alt + Shift + Q`
- **Fullscreen Toggle:** `Ctrl + Alt + Shift + F`
- **Note:** Must be launched with `DISPLAY=:0` when accessed via SSH — NoMachine conflicts with physical HDMI output. Use `sudo systemctl restart display-manager` to restore physical display if NoMachine takes over.

### Fire TV (Secondary Client)
- Moonlight app installed via Fire TV app store
- Connects over Wi-Fi to 192.168.0.137
- Tested: Arc Raiders on low settings — playable

### Optimized Stream Settings (H.264)
| Setting | Value |
|---------|-------|
| Resolution | 1080p (720p for lower-end clients) |
| FPS | 60 |
| Bitrate | 15-20 Mbps |
| Codec | H.264 (NOT H.265 — Pi lacks GPU for H.265 decode) |

---

## ⚙️ Windows Optimizations Applied

```powershell
# High Performance Power Plan
powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c

# Game Mode
Set-ItemProperty -Path "HKCU:\Software\Microsoft\GameBar" -Name "AutoGameModeEnabled" -Value 1

# Disable Nagle's Algorithm (lower network latency)
# Applied to all network interfaces via registry

# SystemResponsiveness = 10 (more CPU to foreground)
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile" -Name "SystemResponsiveness" -Value 10 -Type DWord

# Gaming task priority
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" -Name "Priority" -Value 6 -Type DWord
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Multimedia\SystemProfile\Tasks\Games" -Name "Scheduling Category" -Value "High" -Type String

# Disable Xbox Game Bar
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\GameDVR" -Name "AppCaptureEnabled" -Value 0
```

### NVIDIA Control Panel Settings
| Setting | Value |
|---------|-------|
| Power Management Mode | Prefer Maximum Performance |
| Shader Cache Size | 10GB |
| Texture Filtering Quality | High Performance |
| Vertical Sync | Off |

---

## 🔑 Key Lessons Learned

### Emulation
- **PCSX2 must be PS2 only** — it will try to load PS1 games via PS2 mode which fails. Use RetroArch + Beetle PSX for all PS1 games.
- **PS1 BIOS must be in the PS2 BIOS folder** — PCSX2 reads from one BIOS directory for both. PS1 BIOS (SCPH series) needs to live alongside PS2 BIOS files.
- **Vulkan causes PCSX2 crashes on this hardware** — always use Direct3D 11.
- **Dolphin 5.0 from winget is 2017** — always use latest portable dev build from dolphin-emu.org.
- **Dolphin portable install** does not require Program Files — lives cleanly in `C:\HoneyDuo\gaming\emulators\dolphin\`.
- **PCSX2 config** lives in `C:\Users\samue\Documents\PCSX2\inis\` NOT AppData — it overwrites on first launch.

### Streaming
- **H.265 causes ghosting on Pi** — Pi 5 lacks dedicated GPU for H.265 decode. Always use H.264.
- **Bitrate sweet spot for Pi:** 15-20 Mbps H.264 at 1080p60
- **Both host and client must be wired** for best results. Wi-Fi works but wired significantly reduces latency.
- **NoMachine conflicts with physical HDMI** on Pi — restart display-manager to restore physical output.
- **Moonlight on Pi requires** `DISPLAY=:0` prefix when launching via SSH.
- **Fire TV Moonlight** works well over Wi-Fi for casual gaming.

### Infrastructure
- **ROM folder structure is network-migration-ready** — when ROMs move to 3070 node, only the path in emulator configs needs updating.
- **Sunshine web UI** is at https://localhost:47990 on the host machine.
- **Sunshine pairs** via PIN entry in web UI — client shows PIN, enter in Sunshine UI.

---

## 🗺️ Future Tasks

- [ ] Migrate ROM library to 3070 Ti node (network share)
- [ ] Set up 3070 Ti as primary Sunshine host
- [ ] Configure network share so 1070 node can access ROMs from 3070
- [ ] Add GameCube ROM test
- [ ] Add Uptime Kuma monitoring for Sunshine port (47990)
- [ ] Add this node to honey-duo-infrastructure GitHub repo
- [ ] Consider Moonlight as permanent Pi display (retire NoMachine for gaming use)
- [ ] Install NVIDIA drivers update on 1070 node
- [ ] Test Moonlight from additional clients (phones, tablets)

---

## 📦 BIOS Inventory

### PS1 BIOS (stored in `C:\HoneyDuo\gaming\bios\ps2\`)
- NTSC-UC (USA): ps-20a, ps-21a, ps-22a, ps-30a, ps-41a, psone-44a, psone-45a
- NTSC-J (Japan): ps-10j through psone-43j
- PAL-E (Europe): ps-20e through psone-45e
- Misc: SCPH18000.BIN (Japanese), DTLH2000.BIN, ps1_rom.bin

### PS2 BIOS (stored in `C:\HoneyDuo\gaming\bios\ps2\`)
- Full set — 69 total BIOS files covering versions 0100j through 0230e (2000–2008)
- **Active BIOS:** ps2-0230a-20080220.bin (latest USA)