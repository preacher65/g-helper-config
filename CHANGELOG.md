# 📦 G-Helper Config — Changelog

All notable changes to this project are documented in this file using [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format.

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
'git a