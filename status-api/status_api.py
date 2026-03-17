from flask import Flask, jsonify
from flask_cors import CORS
import socket, time, os

app = Flask(__name__)
CORS(app)

# Public (Lubuntu) and Pi IPs can be overridden via env
PUB = os.getenv("JUICY_PUBLIC_IP", "104.8.77.206")
PI  = os.getenv("JUICY_PI_IP",     "192.168.1.73")

# Simple 30s cache so we don't hammer ports
_cache, _stamp = {}, 0

def check_tcp(host: str, port: int, timeout: float = 3.0) -> bool:
    """DNS-aware TCP connect with timeout; returns True if port open."""
    try:
        # Resolve hostnames to IPv4 if needed
        if not host.replace('.', '').isdigit():
            host = socket.gethostbyname(host)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        ok = (s.connect_ex((host, port)) == 0)
        s.close()
        return ok
    except Exception:
        return False

def up(host: str, port: int) -> bool:
    """Cached reachability check (30s window)."""
    global _cache, _stamp
    now = time.time()
    key = (host, port)
    if now - _stamp > 30:
        _cache.clear()
        _stamp = now
    if key not in _cache:
        _cache[key] = check_tcp(host, port)
    return _cache[key]

# --- Optional: AMP player counts (template stub) ---
def get_amp_players():
    """
    Return a dict like:
      {"Minecraft": {"players": 2, "max": 20}, "Valheim": {"players": 0, "max": 10}}
    or None to skip. Implement later against AMP API if desired.
    """
    return None

@app.get("/api/status")
def status():
    players = get_amp_players() or {}

    data = {
        # --- Host (public) services through Traefik domains ---
        "amp": {
            "name": "AMP Panel",
            "type": "web",
            "url": "http://amp.jkeasy.com:8080",
            "status": "running" if up(PUB, 8080) else "stopped",
        },
        "ai": {
            "name": "Juicy AI",
            "type": "ai",
            "url": "https://ai.jkeasy.com",
            "status": "running" if up("ai.jkeasy.com", 443) else "stopped",
        },
        "vault": {
            "name": "Vaultwarden",
            "type": "password",
            "url": "https://vault.jkeasy.com",
            "status": "running" if up("vault.jkeasy.com", 443) else "stopped",
        },
        "dashboard": {
            "name": "Juicy Panel",
            "type": "home",
            "url": "https://dashboard.jkeasy.com",
            "status": "running" if up("dashboard.jkeasy.com", 443) else "stopped",
        },

        # --- Game servers (public ports) ---
        "minecraft": {
            "name": "JuicyCraft",
            "type": "game",
            "url": "minecraft.jkeasy.com:25565",
            "status": "running" if up(PUB, 25565) else "stopped",
            "players": players.get("Minecraft", {}).get("players"),
        },
        "valheim": {
            "name": "Valheim",
            "type": "game",
            "url": "valheim.jkeasy.com:2456",
            "status": "running" if up(PUB, 2456) else "stopped",
            "players": players.get("Valheim", {}).get("players"),
        },

        # --- Raspberry Pi services (LAN ports) ---
        # Map UI (tar1090) on Ultrafeeder
        "ultrafeeder": {
            "name": "Ultrafeeder",
            "type": "flight",
            "url": "https://flights.jkeasy.com",
            "status": "running" if up(PI, 8080) else "stopped",
        },
        # FR24 web status proxied to :8755 -> :8754 in container
        "fr24": {
            "name": "FlightRadar24",
            "type": "flight",
            "url": "https://fr24.jkeasy.com",
            "status": "running" if up(PI, 8755) else "stopped",
        },
        # FlightAware (piaware/skyaware) UI on :8081
        "piaware": {
            "name": "FlightAware",
            "type": "flight",
            "url": "https://piaware.jkeasy.com",
            "status": "running" if up(PI, 8081) else "stopped",
        },
        # RadarBox doesn't expose a web UI by default; we show feeder socket reachability.
        # Using 30005 (Beast) to reflect feeder health.
        "rbfeeder": {
            "name": "RadarBox",
            "type": "flight",
            "url": "https://rb.jkeasy.com",   # Traefik can still proxy to something if desired
            "status": "running" if up(PI, 30005) else "stopped",
        },

        # --- Home stack on Pi ---
        "homeassistant": {
            "name": "Home Assistant",
            "type": "home",
            "url": "https://homeassistant.jkeasy.com",
            "status": "running" if up(PI, 8123) else "stopped",
        },
        "mealie": {
            "name": "Mealie",
            "type": "food",
            "url": "https://mealie.jkeasy.com",
            "status": "running" if up(PI, 9090) else "stopped",
        },
    }
    return jsonify(data)

# ------------------------
# New placeholder endpoints
# ------------------------

@app.get("/api/metrics")
def metrics():
    """
    Placeholder metrics until real collection is implemented.
    Later: expose CPU%, RAM%, Disk% for Lubuntu; CPU%/RAM% for the Pi.
    """
    return jsonify({
        "host": {"cpu": "pending", "ram": "pending", "disk": "pending"},
        "pi":   {"cpu": "pending", "ram": "pending"}
    })

@app.get("/api/flight-summary")
def flight_summary():
    """
    Placeholder summary for Flight Hub tile.
    Later: parse Ultrafeeder JSON (e.g., /data/receiver.json) for aircraft count
    and MLAT status; combine with feeder reachability for a quick health view.
    """
    return jsonify({
        "aircraft": "pending",
        "mlat": "pending",
        "feeder_health": {
            "ultrafeeder": "pending",
            "fr24": "pending",
            "piaware": "pending",
            "rbfeeder": "pending"
        }
    })

@app.get("/api/services")
def services():
    """
    Returns a simple service list so the dashboard can build sections
    even before /api/status or other endpoints are fully wired.
    """
    return jsonify({
        "services": [
            "amp","ai","vault","dashboard",
            "minecraft","valheim",
            "ultrafeeder","fr24","piaware","rbfeeder",
            "homeassistant","mealie"
        ]
    })

@app.get("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    # Default Flask dev server (behind Traefik). For production put behind reverse proxy.
    app.run(host="0.0.0.0", port=5000)
