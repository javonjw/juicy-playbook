# 🧃 Juicy Playbook v1.0

[![Build PDF](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml)

A complete infrastructure playbook for the **Juicy Server Stack**:

- 🖥️ **Lubuntu Host** (AMP, AI, Vaultwarden, NPM)
- 🥧 **Raspberry Pi** (Home Assistant, Flight Tracking, Mealie)

---

## 🚀 **WORKING SERVICES (March 18, 2026)**

### 🖥️ Lubuntu Host (104.8.77.206)
| Service | URL | Port |
|---------|-----|------|
| AMP Game Servers | `http://amp.jkeasy.com:8080` | 8080 |
| Open WebUI (AI) | `http://104.8.77.206:3001` | 3001 |
| Vaultwarden | `http://104.8.77.206:8082` | 8082 |
| Nginx Proxy Manager | `http://104.8.77.206:81` | 81 |

### 🥧 Raspberry Pi (192.168.1.200)
| Service | URL | Port |
|---------|-----|------|
| Flight Radar Map | `http://192.168.1.200:8080` | 8080 |
| FlightAware | `http://192.168.1.200:8081` | 8081 |
| Flightradar24 | `http://192.168.1.200:8755` | 8755 |
| Home Assistant | `http://192.168.1.200:8123` | 8123 |
| Mealie | `http://192.168.1.200:9090` | 9090 |

---

## 🔧 **QUICK COMMANDS**

### Lubuntu Host
```bash
# Check services
docker ps
sudo ss -tulpn | grep -E ":(8080|3001|8082|81)"
