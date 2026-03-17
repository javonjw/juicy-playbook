# Development Notes

A personal workspace for ideas, reminders, commands, configurations, and future plans for the **Juicy Playbook** project.

This page replaces GitHub Wiki (not available on private repos).

---

## 🧠 Quick Notes

- Public IP: 104.8.77.206  
- Pi IP: 192.168.1.73  
- Traefik is handling all domains via Coolify  
- Status API port: 5000  
- Dashboard is static HTML served over NGINX  

---

## 🛰️ Flight Stack Notes (ADS‑B)

- Ultrafeeder: port **8080**  
- FlightRadar24: port **8755**  
- FlightAware SkyAware: port **8081**  
- RadarBox feeder: port **30005**  

To add later:
- Unified Flight Hub tile  
- Aircraft count from `data/receiver.json`  
- MLAT stats from `data/stats.json`

---

## 🎮 Game Server Stack (AMP)

Planned tasks:
- Pull real player counts  
- Support Valheim/Minecraft tiles  
- Clean fallback when offline  
- AMP API token needed when back home

---

## 🖥️ Metrics

Planned `/api/metrics` endpoint:
- CPU%, RAM%, Disk% for Lubuntu host  
- CPU%, RAM% for Raspberry Pi  
- 5–10 second update rate

---

## 🧪 Future Dashboard Ideas

- Color-coded tiles  
- Light/dark mode toggle  
- Grouped tile layout:
  - Games
  - Flight
  - Home
  - System
  - Services  

---

## 📝 Random To‑Dos

- Add “settings.json” sample for Status API  
- Add a `docker-compose.yml` for local testing  
- Add dev notes for Mealie ↔ HA sidebar iframe  
- Improve icons for tile categories  
