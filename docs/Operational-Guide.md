# 📝 **COMPLETE JUICY PLAYBOOK UPDATE**

Copy and paste this entire section into your `docs/Operational-Guide.md`:

---

## 🖥️ **LUBUNTU HOST SERVER - CURRENT STATE (March 2026)**

### ✅ WORKING & CONFIGURED

| Component | Status | Details |
|-----------|--------|---------|
| **Docker** | ✅ Working | Core container runtime |
| **Nginx Proxy Manager** | ✅ Working | Replaced Traefik, handles all reverse proxy |
| **Coolify** | ✅ Working | PaaS manager on port 8000 |
| **AMP Game Servers** | ✅ Working | Native install, port 8080 |
| **Ollama** | ✅ Working | Local AI with Phi-3 Mini model |
| **Open WebUI** | ✅ Working | Chat interface for Ollama |

---

### 📊 **PORT MAP**

| Service | Port | Status | Notes |
|---------|------|--------|-------|
| **AMP** | 8080 | ✅ In Use | Native install, game server management |
| **NPM (HTTP)** | 80 | ✅ In Use | Standard HTTP |
| **NPM (HTTPS)** | 443 | ✅ In Use | Standard HTTPS |
| **NPM (Admin)** | 81 | ✅ In Use | Nginx Proxy Manager web UI |
| **Coolify** | 8000 | ✅ In Use | PaaS manager |
| **Open WebUI** | 3001 | ✅ In Use | AI chat interface |
| **Ollama API** | 11434 | ✅ In Use | Backend for AI models |
| **SSH** | 22 | ✅ In Use | Remote access |

---

### 🌐 **NETWORK CONFIGURATION**

| Setting | Value |
|---------|-------|
| **Public IP** | `104.8.77.206` |
| **Hostname** | `juicy-server` |
| **DNS Records** | `amp.jkeasy.com` → `104.8.77.206` |
| **Firewall** | UFW active, ports 22,80,443,81,8000,8080,3001,11434 open |
| **Swap** | 16GB on SSD, swappiness=30 |

---

### 🐳 **DOCKER NETWORK NOTES**

| Connection | Method |
|------------|--------|
| **NPM → AMP** | `http://172.17.0.1:8080` (Docker bridge) |
| **Open WebUI → Ollama** | `http://localhost:11434` (host network) |
| **Test NPM to AMP** | `docker exec -it npm curl http://172.17.0.1:8080` |
| **Test Open WebUI to Ollama** | `docker exec open-webui curl http://localhost:11434` |

---

### 🤖 **AI SERVICES**

#### Ollama Installation
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull and run Phi-3 Mini
ollama run phi3:mini

# List available models
ollama list

# API endpoint
curl http://localhost:11434/api/tags
```

#### Open WebUI Installation
```bash
# Run Open WebUI in host mode with custom port
docker run -d --network host \
  -v open-webui:/app/backend/data \
  -e WEBUI_PORT=3001 \
  -e PORT=3001 \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main

# Access at: http://104.8.77.206:3001
```

#### Open WebUI Configuration
| Setting | Value |
|---------|-------|
| **Ollama API URL** | `http://localhost:11434` |
| **Default Model** | `phi3:mini` |
| **Admin Account** | Create on first login |

---

### 🔧 **SYSTEM OPTIMIZATION**

#### Swap Configuration (16GB)
```bash
# Create 16GB swap
sudo fallocate -l 16G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make permanent
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Set swappiness to 30 (balanced for AI + general use)
echo 'vm.swappiness=30' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

#### Firewall Rules
```bash
# Essential ports
sudo ufw allow ssh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 81/tcp
sudo ufw allow 8000/tcp
sudo ufw allow 8080/tcp
sudo ufw allow 3001/tcp

# Enable firewall
sudo ufw --force enable
```

---

### 🔍 **TROUBLESHOOTING COMMANDS**

```bash
# Check AMP status
sudo ss -tulpn | grep 8080

# Check Open WebUI
docker ps | grep open-webui
docker logs open-webui --tail 50

# Check Ollama
curl http://localhost:11434/api/tags
ollama list

# Check NPM to AMP connection
docker exec -it npm curl -I http://172.17.0.1:8080

# Check memory and swap
free -h

# Check open ports
sudo ss -tulpn
```

---

### 📝 **NPM PROXY HOST CONFIGURATION**

| Domain | Forward IP | Port | Notes |
|--------|------------|------|-------|
| `amp.jkeasy.com` | `172.17.0.1` | 8080 | AMP Game Server |
| `chat.jkeasy.com` | `172.17.0.1` | 3001 | Open WebUI (optional) |

**Websockets must be enabled** for AMP and Open WebUI.

---

### 🎯 **PERFORMANCE NOTES**

- **Gaming Mode**: AMP uses ~2GB RAM, leaving ~5.6GB free
- **AI Mode**: Phi-3 Mini uses ~2-3GB RAM, swap provides safety net
- **Running Both**: Not recommended simultaneously, but 16GB swap prevents crashes

---

### 🔄 **BACKUP LOCATIONS**

| Service | Data Location |
|---------|---------------|
| **AMP** | `/opt/amp/` |
| **Open WebUI** | Docker volume: `open-webui` |
| **Ollama Models** | `/home/ampserver/.ollama/models/` |
| **NPM Data** | Docker volume (check with `docker volume ls`) |

---

### 🏁 **QUICK START GUIDE**

1. **Access AMP**: `http://amp.jkeasy.com:8080` or `http://104.8.77.206:8080`
2. **Access AI Chat**: `http://104.8.77.206:3001`
3. **Login credentials**: Created during first-time setup
4. **Default AI model**: `phi3:mini`

---

## ✅ **VERIFICATION CHECKLIST**

- [ ] AMP accessible at `http://amp.jkeasy.com:8080`
- [ ] Open WebUI accessible at `http://104.8.77.206:3001`
- [ ] Phi-3 Mini model loads and responds
- [ ] NPM proxy working for AMP
- [ ] 16GB swap active (`free -h`)
- [ ] Firewall rules correct (`sudo ufw status`)

---

## 🚀 **NEXT STEPS / TO-DO**

- [ ] Install Vaultwarden (password manager) on port 8081
- [ ] Set up automated backups
- [ ] Configure monitoring/alerting
- [ ] Add more Ollama models as needed
- [ ] Set up `chat.jkeasy.com` subdomain in NPM

---

**Last Updated:** March 18, 2026  
**Author:** Javon  
**System:** Juicy Server Stack v1.0

---

Copy all of the above and paste it into your `docs/Operational-Guide.md` file! This captures everything we've done today.
