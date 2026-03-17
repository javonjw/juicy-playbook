
from flask import Flask, jsonify
from flask_cors import CORS
import socket, time, os

app = Flask(__name__)
CORS(app)

PUB = os.getenv("JUICY_PUBLIC_IP", "104.8.77.206")
PI  = os.getenv("JUICY_PI_IP",     "192.168.1.73")

_cache, _stamp = {}, 0

def check_tcp(host: str, port: int, timeout: float = 3.0) -> bool:
    try:
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
    global _cache, _stamp
    now = time.time()
    key = (host, port)
    if now - _stamp > 30:
        _cache.clear(); _stamp = now
    if key not in _cache:
        _cache[key] = check_tcp(host, port)
    return _cache[key]

# --- Optional: AMP player counts template ---

def get_amp_players():
    # Return a dict like {"Minecraft": {"players": 2, "max": 20}} or None
    return None

@app.get('/api/status')
def status():
    players = get_amp_players() or {}
    return jsonify({
        "amp":        {"name":"AMP Panel","type":"web","url":"http://amp.jkeasy.com:8080","status":"running" if up(PUB,8080) else "stopped"},
        "ai":         {"name":"Juicy AI","type":"ai","url":"https://ai.jkeasy.com","status":"running" if up("ai.jkeasy.com",443) else "stopped"},
        "vault":      {"name":"Vaultwarden","type":"password","url":"https://vault.jkeasy.com","status":"running" if up("vault.jkeasy.com",443) else "stopped"},
        "dashboard":  {"name":"Juicy Panel","type":"home","url":"https://dashboard.jkeasy.com","status":"running" if up("dashboard.jkeasy.com",443) else "stopped"},
        "minecraft":  {"name":"JuicyCraft","type":"game","url":"minecraft.jkeasy.com:25565","status":"running" if up(PUB,25565) else "stopped","players": players.get('Minecraft',{}).get('players')},
        "valheim":    {"name":"Valheim","type":"game","url":"valheim.jkeasy.com:2456","status":"running" if up(PUB,2456) else "stopped","players": players.get('Valheim',{}).get('players')},
        "flights":    {"name":"Flight Tracker","type":"flight","url":"https://flights.jkeasy.com","status":"running" if up(PI,8080) else "stopped"},
        "homeassistant":{"name":"Home Assistant","type":"home","url":"https://homeassistant.jkeasy.com","status":"running" if up(PI,8123) else "stopped"},
        "mealie":     {"name":"Mealie","type":"food","url":"https://mealie.jkeasy.com","status":"running" if up(PI,9090) else "stopped"},
    })

@app.get('/health')
def health():
    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
