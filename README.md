# 🧃 Juicy Server Stack — Production Ready

[![Build PDF](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml)
![Version](https://img.shields.io/github/v/release/javonjw/juicy-playbook)
![License](https://img.shields.io/github/license/javonjw/juicy-playbook)

## 🚀 Working Services (March 2026)

### 🖥️ Lubuntu Host
| Service | URL | Status |
|---------|-----|--------|
| AMP Game Servers | https://amp.jkeasy.com:8080 | ✅ Running |
| Juicy Dashboard | http://104.8.77.206:8085 | ✅ Running |
| Status API | http://104.8.77.206:5000/api/status | ✅ Running |
| Minecraft Server | minecraft.jkeasy.com:25565 | ✅ Running |
| Coolify | http://104.8.77.206:8000 | ✅ Running |

### 🥧 Raspberry Pi
| Service | URL | Status |
|---------|-----|--------|
| Flight Radar Map | https://flights.jkeasy.com | ✅ Running |
| FlightAware | https://piaware.jkeasy.com | ✅ Running |
| Home Assistant | https://homeassistant.jkeasy.com | ✅ Running |
| Mealie | https://mealie.jkeasy.com | ✅ Running |

## 🏗️ Architecture

- **Router**: AT&T BGW320-500 with IP Passthrough
- **Public IP**: 104.8.77.206
- **Main Server**: Ubuntu 24.04 LTS
- **Pi**: Ethernet IP 192.168.1.204 (primary), WiFi backup
- **SSH**: Port 2222 forwarded to main server

## 🔧 Quick Commands

```bash
# Check status
curl -s http://104.8.77.206:5000/api/status | python3 -m json.tool

# Restart services
docker restart juicy-dashboard status-api

# SSH to main server
ssh ampserver@104.8.77.206 -p 2222

# SSH to Pi
ssh juicy@192.168.1.204
