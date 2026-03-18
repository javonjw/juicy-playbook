# Juicy Stack - Current Working State
*Last updated: March 18, 2026*

## 🖥️ Lubuntu Host (juicy-server)
| Service | Type | Port | Access | Notes |
|---------|------|------|--------|-------|
| AMP | Native | 8080 | `amp.jkeasy.com:8080` | Backend `172.17.0.1:8080` |
| NPM | Docker | 80/443 | `npm.jkeasy.com` | Forwards to AMP via bridge |
| Coolify | Docker | 8000 | `coolify.jkeasy.com` | Working |
| Status API | Docker | 5000 | `status-api:5000` | Internal |
| Juicy Dashboard | Docker | 80 | `juicy-dashboard:80` | Internal |

## 🌐 Network Configuration
- **Public IP**: `104.8.77.206`
- **DNS**: `amp.jkeasy.com` A record → `104.8.77.206`
- **Firewall**: UFW active, ports 22, 80, 443, 8080 open
- **Docker Bridge**: `172.17.0.1` (host gateway)

## 🧪 Verified Working Commands
```bash
# Test AMP locally
curl -I http://127.0.0.1:8080

# Test AMP from NPM container
docker exec -it npm curl -I http://172.17.0.1:8080

# Check AMP status
sudo ss -tulpn | grep 8080
