# 🧃 Juicy Tailscale Stack - Live Production Setup 
 
**Last Updated:** April 14, 2026 
 
## 📡 Network Architecture 
 
This stack runs on a **Tailscale mesh network** - no port forwarding required! 
 
 
## 🖥️ Main Server Services 
 
 
### Internal Only (No Direct Access) 
- Redis cache (redis:6379) 
- PostgreSQL DB (nextcloud-db:5432) 
 
## 🥧 Pi Services 
 
 
## 🔧 Quick Access Commands 
 
```bash 
# SSH to Main Server 
tailscale ssh amp@100.78.0.29 
 
# SSH to Pi 
tailscale ssh pi@100.116.70.56 
 
# Check all containers on Main 
tailscale ssh amp@100.78.0.29 "docker ps" 
 
# Check all containers on Pi 
tailscale ssh pi@100.116.70.56 "docker ps" 
``` 
