## G-Helper Config Project – ASUS ROG Zephyrus G14 (2024)

This repository tracks version-controlled configurations for **G-Helper**, used to tune power, thermal, and fan behavior on the 2024 ROG Zephyrus G14 GA403UI.

The project emphasizes **thermal stability**, **acoustic comfort**, and **GPU-optimized performance**, with tooling and documentation to support consistent config iteration and benchmarking.

---

### 📂 Repository Structure

- `config/` – Saved versions of `config.json`
- `tools/` – Scripts for config diffing, validation, and conversion
- `docs/` – Documentation and tuning references
- `default_config.json` – Stock reference configuration
- `personal_config.json` – Persistent user-level custom settings baseline

---

### 🧹 Design Goals & Principles

- **GPU-first Power Allocation:** Profiles like Turbo and Quiet Gaming prioritize GPU wattage for gaming and rendering.
- **Thermal Management:** All active profiles (except Eco/Silent) include a fail-safe data point at **98 °C**.
- **Fan Curve Logic:**
  - **0% fan duty** only allowed in **Silent** and **Eco+** modes.
  - All other profiles enforce **non-zero minimums** (typically 6–8%) for reliability.
- **Undervolting Strategy:**
  - **CPU undervolt** set in G-Helper where appropriate
  - **GPU undervolt** applied manually via MSI Afterburner profiles
- **Hybrid GPU Mode:** Default setting is **Optimized (auto iGPU/dGPU switching)**.
- **Windows Power Mode:** Defaults to **Balanced** for AC and battery.

---

### ⚙️ Active Profiles (config.json)

| Profile      | Slot | Hotkey | Role                    | CPU Power (W) | GPU Power (W)          | Fan Profile      | Notes                               |
| ------------|------|--------|-------------------------| ------------- | ---------------------- | ---------------- | ----------------------------------- |
| Balanced     | `_0` | F16    | Default for general use | 35/45/55      | 65 (55+10)             | Custom + 98 °C    | Efficient boost, steady ramp        |
| Turbo        | `_1` | F17    | Gaming (Hybrid)         | 55/65/75      | 75 (55+20)             | Aggressive + 98 °C | Prioritized GPU, fan curve tuned    |
| Silent       | `_2` | F18    | Quiet use               | 15/20/25      | 60 (55+5)              | Silent tuned     | Fans off when idle                  |
| Quiet Gaming | `_3` | F19    | Thermally smooth gaming | 15/20/25      | 61 (56+5)              | Custom + 98 °C    | GPU undervolt via Afterburner       |
| Eco+         | `_4` | F20    | Passive light use       | 8/10/15       | 60 (55+5), 400 MHz cap | Passive tuned    | 0 RPM at idle, power capped         |

> Stock profiles:
> - `_5`: Balanced (Stock)
> - `_6`: Turbo (Stock)
> - `_7`: Silent (Stock)

#### 🔑 Virtual Hotkeys
- G-Helper internally maps **profiles `_0` to `_4`** to **F16 to F20**.
- These can be triggered programmatically (e.g. with AutoHotKey) even though those keys don’t exist on standard keyboards.

---

### 🧠 Global G-Helper Settings (included in all configs)

```json
"gpu_auto": 1,
"charge_limit": 80,
"charge_full": 0,
"performance_mode": 0,
"performance_1": 0,
"performance_0": 0
```

These ensure:
- Battery life extension
- Optimized GPU mode
- Balanced Windows power mode on AC and battery

---

### 🛠️ Tooling

- `diff_config.py`: Compare two `config.json` files, output Markdown or CSV summaries
- `validate_config.py`: Check structure and flag errors or drift
- Built using **Python 3.13**, compatible with **VS Code** for editing

---

### 📘 Notes

- All tuning reflects validated behavior specific to the **GA403UI (2024) G14 model**
- Future `config.json` versions are tracked via `config_vX.Y.json` naming
- See `CHANGELOG.md` for version-specific deltas (starting from 1.0)
