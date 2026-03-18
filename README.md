# 🧃 Juicy Playbook v1.0

[![Build PDF](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml)
![Version](https://img.shields.io/github/v/release/javonjw/juicy-playbook)
![License](https://img.shields.io/github/license/javonjw/juicy-playbook)
![Repo Size](https://img.shields.io/github/repo-size/javonjw/juicy-playbook)
![Issues](https://img.shields.io/github/issues/javonjw/juicy-playbook)

A complete infrastructure playbook for building and maintaining the **Juicy Server Stack**:
a hybrid system using:

- 🖥️ **Lubuntu Host Server** (Docker, Coolify, Nginx Proxy Manager, Ollama, Vaultwarden, AMP Game Servers)
- 🥧 **Raspberry Pi (JuicyPi)** (Home Assistant, Mosquitto, Mealie, ADS‑B Feeder Stack)
- 📊 **Juicy Panel** (Status API + front-end dashboard)
- 🤖 **GitHub Automation** (PDF builds, versioning, releases)

---

## 🚀 **CURRENT WORKING STATUS (March 2026)**

### ✅ **Lubuntu Host - Fully Operational**

| Service | Status | Access | Port |
|---------|--------|--------|------|
| **AMP Game Servers** | ✅ Working | `http://amp.jkeasy.com:8080` | 8080 |
| **Nginx Proxy Manager** | ✅ Working | `http://104.8.77.206:81` | 80/443/81 |
| **Open WebUI** | ✅ Working | `http://104.8.77.206:3001` | 3001 |
| **Vaultwarden** | ✅ Working | `http://104.8.77.206:8082` | 8082 |
| **Ollama + Phi-3 Mini** | ✅ Working | Local API on 11434 | 11434 |
| **Coolify** | ✅ Working | `http://104.8.77.206:8000` | 8000 |
| **Docker** | ✅ Working | Container runtime | N/A |

---

## 📊 **PORT MAP**

| Service | Port | Notes |
|---------|------|-------|
| SSH | 22 | Remote access |
| HTTP | 80 | NPM |
| HTTPS | 443 | NPM with SSL |
| NPM Admin | 81 | Nginx Proxy Manager UI |
| Coolify | 8000 | PaaS manager |
| AMP | 8080 | Game server management |
| Vaultwarden | 8082 | Password manager |
| Open WebUI | 3001 | AI chat interface |
| Ollama API | 11434 | Local AI backend |

---

## 🌐 **NETWORK CONFIGURATION**

- **Public IP**: `104.8.77.206`
- **Hostname**: `juicy-server`
- **DNS Records**:
  - `amp.jkeasy.com` → `104.8.77.206`
  - `vault.jkeasy.com` → `104.8.77.206` (optional)
- **Firewall**: UFW active with all above ports open
- **Swap**: 16GB on SSD, swappiness=30

---

## 🐳 **DOCKER NETWORK NOTES**

| Connection | Method |
|------------|--------|
| NPM → AMP | `http://172.17.0.1:8080` |
| Open WebUI → Ollama | `http://localhost:11434` |
| NPM → Vaultwarden | `http://172.17.0.1:8082` |

---

## 🤖 **AI SERVICES**

### Ollama
```bash
# Install
curl -fsSL https://ollama.com/install.sh | sh

# Run Phi-3 Mini
ollama run phi3:mini

# API endpoint
curl http://localhost:11434/api/tags
