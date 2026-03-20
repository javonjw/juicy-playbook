# 🧃 Juicy Playbook v1.0

[![Build PDF](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml)
![Version](https://img.shields.io/github/v/release/javonjw/juicy-playbook)
![License](https://img.shields.io/github/license/javonjw/juicy-playbook)

A complete infrastructure playbook for building and maintaining the **Juicy Server Stack**:

- 🖥️ **Lubuntu Host** (AMP, AI, Vaultwarden, Coolify, Traefik, Juicy Dashboard)
- 🥧 **Raspberry Pi** (Home Assistant, Flight Tracking, Mealie)
- 📊 **Juicy Panel** (Status API + front-end dashboard)
- 🤖 **GitHub Automation** (PDF builds, versioning, releases)

---

## 🚀 **WORKING SERVICES (March 20, 2026)**

### 🖥️ **Lubuntu Host (juicy-server) - 104.8.77.206**
| Service | URL | Port | Status |
|---------|-----|------|--------|
| AMP Game Servers | `https://amp.jkeasy.com` | 8080 | ✅ Working |
| Open WebUI (AI) | `http://104.8.77.206:3001` | 3001 | ✅ Working |
| Vaultwarden | `https://vault.jkeasy.com` | (Coolify) | ✅ Working |
| Coolify | `http://104.8.77.206:8000` | 8000 | ✅ Working |
| Juicy Dashboard | `https://dashboard.jkeasy.com` | 8085 | ✅ Working |
| Status API | Internal | 5000 | ✅ Working |
| Traefik Proxy | `http://104.8.77.206` | 80/443 | ✅ Working |

### 🥧 **Raspberry Pi (juicypi) - 192.168.1.200**
| Service | URL | Port | Status |
|---------|-----|------|--------|
| Flight Radar Map | `https://flights.jkeasy.com` | 8080 | ✅ Working |
| FlightAware | `https://piaware.jkeasy.com` | 8081 | ✅ Working |
| Flightradar24 | `https://fr24.jkeasy.com` | 8755 | ✅ Working |
| Home Assistant | `https://homeassistant.jkeasy.com` | 8123 | ✅ Working |
| Mealie | `https://mealie.jkeasy.com` | 9090 | ✅ Working |

---

## 🤖 **AI MODELS (Ollama)**

All models available in Open WebUI at `http://104.8.77.206:3001`

### Lightning Fast Models
| Model | Size | Use Case |
|-------|------|----------|
| `qwen2.5:0.5b` | 350 MB | Ultra-fast Q&A |
| `tinyllama` | 750 MB | General chat |
| `smollm:1.7b` | 1.1 GB | Simple tasks |
| `phi` | 1.6 GB | Smart & fast |
| `gemma2:2b` | 1.5 GB | Google's efficient |

### Coding Specialists
| Model | Size | Use Case |
|-------|------|----------|
| `deepseek-coder:1.3b` | 650 MB | HTML/CSS/JS |
| `codeqwen:1.5b` | 900 MB | Code specialist |
| `codegemma:2b` | 1.5 GB | Google's coding |
| `stable-code:3b` | 1.7 GB | Best balance |
| `codellama:7b` | 3.8 GB | Complex tasks |

### Jan-Code 4B Variants
| Model | Size | Quality |
|-------|------|---------|
| `jan-code-q4ks` | 2.6 GB | Fastest |
| `jan-code-q4km` | 2.7 GB | **Best balance** |
| `jan-code-q5km` | 3.2 GB | Higher quality |
| `jan-code-q80` | 4.7 GB | Near-lossless |

### Document & Vision
| Model | Size | Use Case |
|-------|------|----------|
| `moondream` | 1.6 GB | OCR, image text |
| `llava:7b` | 4.2 GB | Image Q&A |
| `minicpm-v` | 2.8 GB | Document Q&A |
| `nomic-embed-text` | 274 MB | Document search |

---

## 📊 **COMPLETE PORT MAP**

### Lubuntu Host Ports
| Port | Service | Purpose |
|------|---------|---------|
| 22 | SSH | Remote access |
| 80 | HTTP | Traefik (redirects to HTTPS) |
| 443 | HTTPS | Traefik with SSL |
| 8000 | Coolify | PaaS manager |
| 8080 | AMP | Game servers |
| 8085 | Juicy Dashboard | Main status dashboard |
| 5000 | Status API | Backend for dashboard |
| 3001 | Open WebUI | AI chat interface |

### Raspberry Pi Ports
| Port | Service | Purpose |
|------|---------|---------|
| 22 | SSH | Remote access |
| 8080 | Ultrafeeder | Flight radar map |
| 8081 | PiAware | FlightAware status |
| 8755 | FR24feed | Flightradar24 status |
| 8123 | Home Assistant | Home automation |
| 9090 | Mealie | Recipe manager |
| 1883 | Mosquitto | MQTT broker |

---

## 🌐 **NETWORK CONFIGURATION**

### AT&T BGW320-500 Settings
- **IP Passthrough**: Enabled for Lubuntu host
- **Public IP**: `104.8.77.206` (Lubuntu host)
- **DHCP Lease**: 99 days (prevents renewal drops)
- **DHCP Range**: `192.168.1.64 - 192.168.1.253`
- **DNS**: `192.168.1.254`
- **Port Forwarding**: Ports 80, 443 forwarded to `104.8.77.206`

### Firewall Rules (UFW)
```bash
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8000/tcp
sudo ufw allow 8080/tcp
sudo ufw allow 8085/tcp
sudo ufw allow 3001/tcp
sudo ufw allow 5000/tcp
sudo ufw --force enable
