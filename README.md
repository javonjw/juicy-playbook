# 🧃 Juicy Server Stack — Production Ready

A complete infrastructure playbook for building and maintaining the **Juicy Server Stack** with Traefik reverse proxy, Docker, and automatic SSL.

## 🚀 Current Status (March 2026)

### ✅ Working Services

#### 🖥️ Lubuntu Host (juicy-server)
| Service | URL | Status |
|---------|-----|--------|
| AMP Game Servers | https://amp.jkeasy.com:8080 | ✅ Running |
| Open WebUI (AI) | http://YOUR_IP:3001 | ✅ Running |
| Vaultwarden | https://vault.jkeasy.com | ✅ Running |
| Coolify | http://YOUR_IP:8000 | ✅ Running |
| Juicy Dashboard | https://dashboard.jkeasy.com | ✅ Running |
| Status API | https://api.jkeasy.com/api/status | ✅ Running |
| Minecraft Server | minecraft.jkeasy.com:25565 | ✅ Running |

#### 🥧 Raspberry Pi (juicypi - 192.168.1.200)
| Service | URL | Status |
|---------|-----|--------|
| Flight Radar Map | https://flights.jkeasy.com | ⚠️ Needs restart |
| FlightAware | https://piaware.jkeasy.com | ⚠️ Needs restart |
| Flightradar24 | https://fr24.jkeasy.com | ⚠️ Needs restart |
| Home Assistant | https://homeassistant.jkeasy.com | ⚠️ Needs restart |
| Mealie | https://mealie.jkeasy.com | ⚠️ Needs restart |

## 🏗️ Architecture

### Network Setup
- **AT&T BGW320-500**: IP Passthrough enabled
- **Public IP**: 104.8.77.206
- **Traefik**: Reverse proxy with Let's Encrypt SSL
- **Docker Network**: All containers on `coolify` network

### Container Configuration

#### Status API
```bash
docker run -d \
  --name status-api \
  --network coolify \
  -l "traefik.enable=true" \
  -l "traefik.http.routers.status-api.rule=Host(\`api.jkeasy.com\`)" \
  -l "traefik.http.routers.status-api.entrypoints=https" \
  -l "traefik.http.routers.status-api.tls=true" \
  -l "traefik.http.routers.status-api.tls.certresolver=letsencrypt" \
  -l "traefik.http.services.status-api.loadbalancer.server.port=5000" \
  --restart unless-stopped \
  status-api-status-api
