# 📦 G-Helper Config — Changelog

All notable changes to this project are documented in this file using [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

## Version 1.0.1 – Minimum Fan Duty Patch (2025-07-28)

This patch enforces an 8% minimum fan speed for profiles Balanced (`_0`) and Quiet Gaming (`_3`), improving fan startup reliability and long-term endurance.

### 🔧 Changes
- ⬆️ Raised **minimum fan speed** on all fans for `_0` and `_3` to **8%** (from prior 5–6%)
- 🚫 No other power, thermal, or behaviour changes were made
- ✔️ Turbo, Silent, and Eco profiles remain unchanged

### 🔍 Rationale
- Very low fan duties (e.g. 5%) can cause delayed fan spin-up or stalling
- 8% is a safe, quiet floor that improves responsiveness without significant acoustic penalty

---

## v1.0.0 — Initial Release 2025-07-27 16:25

### 🎮 Profiles
- 🧩 Defined `default_config.json`, `personal_config.json`
- ⚙️ Added annotated versions of both configs in `/config/annotated/`

### 🔧 Config Management
- 📁 Organized project folder structure
- 🗃️ Saved `config_reordered_patched.json` as current working setup
- 🧠 Documented default G-Helper settings for Balanced, Turbo, and Silent

### 🧰 Tooling
- 🧮 Initial version of Python diff tool: `tools/diff_config.py`
- 📊 Outputs Markdown + CSV diffs to `docs/diffs/`
- 🔧 Handles CRLF/LF consistency via `.gitattributes`

### 📘 Documentation
- 📁 Added folder structure and usage notes to `README.md`
- 🧠 Documented GPU mode behavior and profile switching
- 🛠 Clarified role of default vs personal configs

### 🧪 Dev Setup
- ✅ Project ready for GitHub workflows
- ⚙️ Supports local VS Code + Python 3.13 dev stack

---
