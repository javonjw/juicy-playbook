# 🧃 Juicy Playbook v1.0

[![Build PDF](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml)

A complete infrastructure playbook for the **Juicy Server Stack**:

- 🖥️ **Lubuntu Host** (AMP, AI, Vaultwarden, NPM, Juicy Dashboard)
- 🥧 **Raspberry Pi** (Home Assistant, Flight Tracking, Mealie)

---

## 🚀 **WORKING SERVICES (March 19, 2026)**

### 🖥️ Lubuntu Host (104.8.77.206)
| Service | URL | Port | Status |
|---------|-----|------|--------|
| AMP Game Servers | `http://104.8.77.206:8080` | 8080 | ✅ ADS01 + Valheim01 |
| Open WebUI (AI) | `http://104.8.77.206:3001` | 3001 | ✅ Working |
| Vaultwarden | `http://104.8.77.206:8082` | 8082 | ✅ Working |
| Nginx Proxy Manager | `http://104.8.77.206:81` | 81 | ✅ Working |
| Juicy Dashboard | `http://104.8.77.206:8085` | 8085 | ✅ Working |
| Status API | Internal | 5000 | ✅ Working |

### 🥧 Raspberry Pi (192.168.1.200)
| Service | URL | Port | Status |
|---------|-----|------|--------|
| Flight Radar Map | `http://192.168.1.200:8080` | 8080 | ✅ Working |
| FlightAware | `http://192.168.1.200:8081` | 8081 | ✅ Working |
| Flightradar24 | `http://192.168.1.200:8755` | 8755 | ✅ Working |
| Home Assistant | `http://192.168.1.200:8123` | 8123 | ✅ Working |
| Mealie | `http://192.168.1.200:9090` | 9090 | ✅ Working |

---

## 🔧 **QUICK COMMANDS**

### Lubuntu Host
```bash
# Check all Docker services
docker ps

# Check AMP instances
ps aux | grep -i amp

# Test AMP
curl -I http://localhost:8080
