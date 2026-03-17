
# JUICY PLAYBOOK v1.0 (Clean Install · March 2026)

This repository contains everything required to rebuild the **Juicy** stack on **Lubuntu 24.04** (ThinkCentre M83) and a **Raspberry Pi** (JuicyPi):

- Coolify + Traefik reverse proxy (SSL)
- Vaultwarden, Open WebUI + Ollama, Uptime Kuma (optional Portainer CE)
- AMP for game servers (Minecraft, Valheim, etc.)
- **Juicy Panel** (Status API + static frontend)
- Raspberry Pi services: Home Assistant, Mosquitto, Mealie, Ultrafeeder + FR24 + FlightAware + RadarBox
- DNS (Squarespace) + dynamic Traefik routes to the Pi
- Backups and runbooks

> ✅ This is the authoritative playbook and file set for a fresh install.

---

## Directory Layout
```
juicy-playbook-v1.0/
├─ README.md
├─ Juicy-Playbook-v1.0.md
├─ Juicy-Playbook-v1.0.pdf
├─ docs/
│  ├─ diagrams-notes.md
│  └─ runbooks.md
├─ scripts/
│  ├─ backup-server.sh
│  └─ verify-services.sh
├─ status-api/
│  ├─ Dockerfile
│  └─ status_api.py
├─ my-dashboard/
│  ├─ Dockerfile
│  └─ index.html
└─ pi/
   └─ docker-compose.yml
```

See `docs/runbooks.md` for common procedures and `scripts/` for helpers.
