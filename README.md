# 🎛️ G-Helper Configurations for ASUS Zephyrus G14 (2024)

This repository contains custom `config.json` setups for [G-Helper](https://github.com/seerge/g-helper), optimized for the **2024 ASUS ROG Zephyrus G14 (GA403UI, RTX 4070)**.

These profiles aim to balance performance, thermals, noise, and power consumption with fine-tuned fan curves, CPU/GPU power limits, and undervolts.

---

## 🧩 Profile Overview

| Profile Label     | CPU Power (W)   | GPU Power (W)   | CPU Boost   | GPU Target / Offset   | Fan Curve            |
|-------------------|-----------------|------------------|-------------|------------------------|----------------------|
| Balanced Plus     | 35 / 45 / 55    | 65 (55+10)       | Enabled     | +75 / +100             | Quiet, tuned         |
| Turbo / Gaming    | 65 / 75 / 85    | 80 (55+25)       | Aggressive  | +75 / +100             | Aggressive ramp      |
| Silent Plus       | 15 / 20 / 25    | 60 (55+5)        | Disabled    | Default                | G-Helper default     |
| Quiet Gaming      | 15 / 20 / 25    | 61 (56+5)        | Disabled    | 1850 @ 800 mV          | Smoothed low-noise   |
| Eco               | 8 / 10 / 15     | 60 (55+5)        | Disabled    | 400 MHz capped         | Passive ultra-low    |
| Stock Balanced    | Default         | Default          | Default     | Default                | Default              |
| Stock Turbo       | Default         | Default          | Default     | Default                | Default              |
| Stock Silent      | Default         | Default          | Default     | Default                | Default              |

> All profiles use GPU Mode: **Optimized (auto-switching)**  
> CPU and GPU fan max RPMs: 6800, Mid fan: 8000

---

## 📁 Repository Structure

g-helper-config/
├── config/
│ ├── default_config.json
│ ├── personal_config.json
│ ├── config_reordered_patched.json
│ └── annotated/
│ ├── annotated_default_config.jsonc.txt
│ └── annotated_personal_config.jsonc.txt
├── docs/
│ ├── PROFILE_OVERVIEW.md
│ └── FAN_CURVES.md
├── tools/
│ └── diff_config.py (coming soon)
├── CHANGELOG.md
└── README.md


---

## 📝 Notes on Behavior

### GPU Mode
- `gpu_auto: 1` — enables Optimized (auto iGPU/dGPU switching)
- `gpu_mode: 1` — MS Hybrid mode (iGPU drives display)

### Performance Modes
- `performance_mode` — current active mode
- `performance_0` — used when on battery
- `performance_1` — used when on AC

### Battery Management
- `charge_limit` — sets max charge % (e.g. 80)
- `charge_full` — override to allow full charge (1 = full)

---

## 💾 How to Use

1. Replace your existing config at: C:\ProgramData\ghelper\config.json
2. Restart G-Helper (run elevated for full effect)
3. Use G-Helper tray or hotkeys to switch profiles

---

## ⚠️ Disclaimer

These configs are tuned for **GA403UI (RTX 4070)** and may not be fully compatible with other systems. Always validate undervolts and power settings before applying long-term use.

---

## 📌 Credits

- Based on [G-Helper by seerge](https://github.com/seerge/g-helper)
- Profile tuning by preacher65
