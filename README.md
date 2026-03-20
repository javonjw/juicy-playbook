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
| Open WebUI (AI) | `https://ai.jkeasy.com` | 3000 | ✅ Working |
| Vaultwarden | `https://vault.jkeasy.com` | (Coolify) | ✅ Working |
| Coolify | `http://104.8.77.206:8000` | 8000 | ✅ Working |
| Juicy Dashboard | `https://dashboard.jkeasy.com` | 8085 | ✅ Working (via Traefik) |
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
| 3000 | Open WebUI | AI chat interface |

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
sudo ufw allow 3000/tcp
sudo ufw allow 5000/tcp
sudo ufw --force enable
