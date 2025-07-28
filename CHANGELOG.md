# G-Helper Config Changelog

## Version 1.0 – Initial Baseline (2025-07-28)

This version establishes the **first clean, validated `config.json`** for the ASUS ROG Zephyrus G14 (2024) – GA403UI model, reflecting everything agreed and applied through the July tuning process.

---

### 🔄 What’s Included

- 🔧 **Profile settings** tuned for each mode (Balanced, Turbo, Silent, Quiet Gaming, Eco+)
- 🌡️ **Temperature limits** and fan fail-safe points applied
- ⚙️ **Hybrid GPU Mode** enabled (Optimized)
- 🔋 **Battery charge limit** enforced at 80%
- 🎚️ **Power sliders** and CPU/GPU Boost logic tuned per profile
- 🌀 **Fan curves** defined for each profile and documented
- 🧩 **Custom Profiles (Slots `_0` to `_4`)**:
  - Defined roles, power allocations, and behavior per slot
- 🧠 **Global overrides** included (e.g. `gpu_auto`, `charge_limit`, `performance_mode`)
- ✅ Confirmed matches between `config.json`, documentation, and intended behavior

---

### 🗂️ Profiles Overview Snapshot (for comparison)

This snapshot reflects the current tuning only; see README for full definitions.

| Profile      | Slot | CPU W  | GPU W      | Fan Fail-safe | GPU Undervolt |
| ------------|------|--------|------------|---------------|----------------|
| Balanced     | `_0` | 35/45/55 | 65 (55+10) | Yes (98 °C)   | Afterburner (manual) |
| Turbo        | `_1` | 55/65/75 | 75 (55+20) | Yes (98 °C)   | Afterburner    |
| Silent       | `_2` | 15/20/25 | 60 (55+5)  | No (0% fans OK) | No |
| Quiet Gaming | `_3` | 15/20/25 | 61 (56+5)  | Yes (98 °C)   | Yes (800 mV)   |
| Eco+         | `_4` | 8/10/15  | 60 (55+5)  | No (Fans 0%)  | No |

---

### 📎 Versioning Convention

- `1.0`: Initial complete baseline config
- Minor updates (e.g. `1.1`) = variable changes (fan, power, boost, limits)
- Major updates (e.g. `2.0`) = structural changes (profile renames, slot reshuffles)

---

### 🔍 Historical Tracking

Tracked under `config/config_v1.0.json`  
See `tools/diff_config.py` for comparing future revisions

---

