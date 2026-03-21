# 🧃 Juicy Server Stack — Production Ready

[![Build PDF](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml)
![Version](https://img.shields.io/github/v/release/javonjw/juicy-playbook)
![License](https://img.shields.io/github/license/javonjw/juicy-playbook)

## 🚀 Working Services (March 2026)

### 🖥️ Main Server
| Service | URL | Status |
|---------|-----|--------|
| AMP Game Servers | https://amp.example.com:8080 | ✅ Running |
| Juicy Dashboard | http://YOUR_IP:8085 | ✅ Running |
| Status API | http://YOUR_IP:5000/api/status | ✅ Running |
| Minecraft Server | minecraft.example.com:25565 | ✅ Running |
| Coolify | http://YOUR_IP:8000 | ✅ Running |

### 🥧 Raspberry Pi
| Service | URL | Status |
|---------|-----|--------|
| Flight Radar Map | https://flights.example.com | ✅ Running |
| FlightAware | https://piaware.example.com | ✅ Running |
| Home Assistant | https://homeassistant.example.com | ✅ Running |
| Mealie | https://mealie.example.com | ✅ Running |

## 🏗️ Architecture

- **Router**: Configured with IP Passthrough
- **Main Server**: Ubuntu 24.04 LTS
- **Pi**: Ethernet (primary), WiFi backup
- **SSH**: Custom port forwarded to main server

## 🔧 Quick Commands

```bash
# Check status
curl -s http://YOUR_IP:5000/api/status | python3 -m json.tool

# Restart services
docker restart juicy-dashboard status-api

# SSH to main server
ssh user@YOUR_IP -p 2222

# SSH to Pi
ssh user@PI_IP
