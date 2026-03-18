# 🧃 Juicy Playbook v1.0

[![Build PDF](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml)
![Version](https://img.shields.io/github/v/release/javonjw/juicy-playbook)
![License](https://img.shields.io/github/license/javonjw/juicy-playbook)
![Repo Size](https://img.shields.io/github/repo-size/javonjw/juicy-playbook)
![Issues](https://img.shields.io/github/issues/javonjw/juicy-playbook)

A complete infrastructure playbook for building and maintaining the **Juicy Server Stack**:
a hybrid system using:

- 🖥️ **Lubuntu Host Server** (Docker, Coolify, Nginx Proxy Manager, Ollama, Vaultwarden, AMP Game Servers)
- 🥧 **Raspberry Pi (JuicyPi)** (Home Assistant, Mosquitto, Mealie, Flight Tracking Stack: Ultrafeeder, PiAware, FR24, RadarBox)
- 📊 **Juicy Panel** (Status API + front-end dashboard)
- 🤖 **GitHub Automation** (PDF builds, versioning, releases)

---

## 🚀 **CURRENT WORKING STATUS (March 18, 2026)**

### 🖥️ **Lubuntu Host (juicy-server) - 104.8.77.206**
| Service | URL | Port | Status |
|---------|-----|------|--------|
| AMP Game Servers | `http://amp.jkeasy.com:8080` | 8080 | ✅ Working |
| Open WebUI (AI) | `http://104.8.77.206:3001` | 3001 | ✅ Working |
| Vaultwarden | `http://104.8.77.206:8082` | 8082 | ✅ Working |
| Nginx Proxy Manager | `http://104.8.77.206:81` | 81 | ✅ Working |
| Coolify | `http://104.8.77.206:8000` | 8000 | ✅ Working |
| Ollama API | Internal | 11434 | ✅ Working |

### 🥧 **Raspberry Pi (juicypi) - 192.168.1.200**
| Service | URL | Port | Status |
|---------|-----|------|--------|
| Flight Radar Map (Ultrafeeder) | `http://192.168.1.200:8080` | 8080 | ✅ Working |
| FlightAware (PiAware) | `http://192.168.1.200:8081` | 8081 | ✅ Working |
| Flightradar24 (FR24) | `http://192.168.1.200:8755` | 8755 | ✅ Working |
| RadarBox (rbfeeder) | Internal | - | ✅ Working |
| Home Assistant | `http://192.168.1.200:8123` | 8123 | ✅ Working |
| Mealie | `http://192.168.1.200:9090` | 9090 | ✅ Working |
| Mosquitto (MQTT) | Internal | 1883 | ✅ Working |

---

## 📊 **COMPLETE PORT MAP**

### Lubuntu Host Ports
| Port | Service | Purpose |
|------|---------|---------|
| 22 | SSH | Remote access |
| 80 | HTTP | Nginx Proxy Manager |
| 81 | NPM Admin | NPM web UI |
| 443 | HTTPS | NPM SSL |
| 3001 | Open WebUI | AI chat interface |
| 8080 | AMP | Game servers |
| 8082 | Vaultwarden | Password manager |
| 8000 | Coolify | PaaS manager |
| 11434 | Ollama API | Local AI backend |

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
- **DHCP Range**: `192.168.1.64 - 192.168.1.253`
- **DNS**: `192.168.1.254`

### WiFi Configuration (CRITICAL)
| Device | Band | SSID | Status |
|--------|------|------|--------|
| Lubuntu Server | 2.4 GHz | `ATTwyKq7BZ` | ✅ Fixed |
| Raspberry Pi | 2.4 GHz | `ATTwyKq7BZ` | ✅ Fixed via BSSID lock |

**Pi WiFi Lock Configuration:**
```bash
# /etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
    ssid="ATTwyKq7BZ"
    psk="t8xz9t73imsw"
    bssid=D0:FC:D0:76:6B:44
    frequency=2412
    scan_freq=2412
}
Update documentation - March 18, 2026
