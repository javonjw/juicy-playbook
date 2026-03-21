**Absolutely!** Now that everything is working perfectly, it's the perfect time to create a clean, updated README for your GitHub repository. Here's a comprehensive README that reflects your current production setup:

---

# 🧃 Juicy Server Stack — Production Ready

[![Build PDF](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml/badge.svg)](https://github.com/javonjw/juicy-playbook/actions/workflows/build-pdf.yml)
![Version](https://img.shields.io/github/v/release/javonjw/juicy-playbook)
![License](https://img.shields.io/github/license/javonjw/juicy-playbook)

A complete infrastructure playbook for building and maintaining the **Juicy Server Stack** — a self-hosted homelab with automatic SSL, reverse proxy, and comprehensive monitoring.

## 🚀 Working Services (March 2026)

### 🖥️ Lubuntu Host (juicy-server)
| Service | URL | Port | Status |
|---------|-----|------|--------|
| AMP Game Servers | https://amp.jkeasy.com | 8080 | ✅ Running |
| Open WebUI (AI) | http://YOUR_IP:3001 | 3001 | ✅ Running |
| Vaultwarden | https://vault.jkeasy.com | (Coolify) | ✅ Running |
| Coolify | http://YOUR_IP:8000 | 8000 | ✅ Running |
| Juicy Dashboard | https://dashboard.jkeasy.com | 8085 | ✅ Running |
| Status API | https://api.jkeasy.com/api/status | 5000 | ✅ Running |
| Minecraft Server | minecraft.jkeasy.com:25565 | 25565 | ✅ Running |

### 🥧 Raspberry Pi (juicypi - 192.168.1.190)
| Service | URL | Port | Status |
|---------|-----|------|--------|
| Flight Radar Map | https://flights.jkeasy.com | 8080 | ✅ Running |
| FlightAware | https://piaware.jkeasy.com | 8081 | ✅ Running |
| Flightradar24 | https://fr24.jkeasy.com | 8755 | ✅ Running |
| Home Assistant | https://homeassistant.jkeasy.com | 8123 | ✅ Running |
| Mealie | https://mealie.jkeasy.com | 9090 | ✅ Running |

## 🏗️ Architecture

### Network Setup
- **AT&T BGW320-500**: IP Passthrough enabled for Lubuntu host
- **Public IP**: 104.8.77.206
- **Traefik**: Reverse proxy with Let's Encrypt SSL
- **Docker Network**: All containers on `coolify` network
- **Raspberry Pi**: Static IP 192.168.1.190 (WiFi/ Ethernet)

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
```

#### Juicy Dashboard
```bash
docker run -d \
  --name juicy-dashboard \
  --network coolify \
  -p 8085:80 \
  -v /opt/juicy-dashboard/config.json:/usr/share/nginx/html/config.json:ro \
  -l "traefik.enable=true" \
  -l "traefik.http.routers.dashboard.rule=Host(\`dashboard.jkeasy.com\`)" \
  -l "traefik.http.routers.dashboard.entrypoints=https" \
  -l "traefik.http.routers.dashboard.tls=true" \
  -l "traefik.http.routers.dashboard.tls.certresolver=letsencrypt" \
  -l "traefik.http.services.dashboard.loadbalancer.server.port=80" \
  --restart unless-stopped \
  ghcr.io/javonjw/juicy-dashboard:latest
```

### Runtime Configuration
Create `/opt/juicy-dashboard/config.json`:
```json
{
  "API_BASE": "https://api.jkeasy.com"
}
```

## 🔧 Troubleshooting

### Dashboard Shows "Cannot Reach API"
1. Verify API is reachable: `curl https://api.jkeasy.com/api/status`
2. Check config.json: `curl https://dashboard.jkeasy.com/config.json`
3. Ensure dashboard container can reach API internally: `docker exec juicy-dashboard curl http://status-api:5000/api/status`

### Raspberry Pi Services Not Starting
```bash
# SSH into Pi
ssh juicy@192.168.1.190

# Start all services
docker start ultrafeeder piaware fr24feed homeassistant mealie

# Check status
docker ps
```

### Fix WiFi on Pi
```bash
# Edit WiFi config
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Add your network
network={
    ssid="YOUR_WIFI"
    psk="YOUR_PASSWORD"
}

# Apply config
sudo wpa_cli -i wlan0 reconfigure
sudo dhcpcd wlan0
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/status` | GET | All service statuses |
| `/api/flight-summary` | GET | Aircraft tracking summary |
| `/api/host` | GET | Host system metrics |
| `/api/pi` | GET | Raspberry Pi metrics |

## 🛠️ Maintenance

### Update Dashboard
```bash
docker pull ghcr.io/javonjw/juicy-dashboard:latest
docker stop juicy-dashboard && docker rm juicy-dashboard
# Run with same command as above
```

### Update Status API
```bash
docker stop status-api && docker rm status-api
# Run with same command as above
```

### View Logs
```bash
# Dashboard logs
docker logs juicy-dashboard --tail 50

# API logs
docker logs status-api --tail 50

# Traefik logs
docker logs coolify-proxy --tail 50
```

## 🔐 Security Notes
- All public services use HTTPS with valid Let's Encrypt SSL certificates
- Traefik handles automatic HTTP→HTTPS redirection
- UFW firewall only exposes ports 80, 443, 22, and service ports
- Status API includes CORS headers for dashboard domain only
- Raspberry Pi is on local network with firewall enabled

## 📈 Monitoring
Add Uptime Kuma for service monitoring:
```bash
docker run -d \
  --name uptime-kuma \
  --network coolify \
  -v /opt/uptime-kuma/data:/app/data \
  -l "traefik.enable=true" \
  -l "traefik.http.routers.kuma.rule=Host(\`monitor.jkeasy.com\`)" \
  -l "traefik.http.routers.kuma.entrypoints=https" \
  -l "traefik.http.routers.kuma.tls=true" \
  --restart unless-stopped \
  louislam/uptime-kuma:latest
```

## 🎯 Quick Commands

### Check Service Status
```bash
curl -s https://api.jkeasy.com/api/status | python3 -m json.tool
```

### Restart All Services
```bash
# Main server
docker restart juicy-dashboard status-api coolify-proxy

# Raspberry Pi
ssh juicy@192.168.1.190 "docker restart ultrafeeder piaware fr24feed homeassistant mealie"
```

---

**Last Updated**: March 21, 2026  
**Status**: ✅ Production Ready  
**Maintainer**: @javonjw

---

