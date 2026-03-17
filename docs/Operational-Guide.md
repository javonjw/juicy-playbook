Got it—sorry about that, Javon. The chat didn’t attach a downloadable file. No worries—we’ll save the guide into your repo in one of these quick ways:

***

## Option A (recommended): Create the file in **GitHub UI**

1.  Go to your repo → **Code** → open the **`docs/`** folder.
2.  Click **Add file → Create new file**.
3.  In the filename box, type exactly:
        docs/Operational-Guide.md
4.  Copy the **entire document** below and paste it into the editor.
5.  Scroll down → **Commit changes** (to `main` or `develop`, your call).

***

## Option B (local Windows PowerShell): Create + push

```powershell
git checkout develop
@'
# Juicy Playbook — End‑to‑End Setup & Ops Guide
*(GitHub‑only now, Home‑lab deploy later)*

> **What you already finished**  
> - Repo pushed and structured  
> - `.gitignore` / `LICENSE` / README  
> - Branches: `main` (stable) + `develop` (work)  
> - Workflows: build PDF, release upload, changelog  
> - Releases: `v1.0.0`, `v1.1.0`  
> - Project Board + automations  
> - Issue templates, labels, priorities, milestones  
> - Docs folder ready  
> - Status API updated (ADS‑B tiles + new endpoints)  
> - Dashboard updated (Flight Hub tile, metrics badges, Pi‑offline banner)

---

## 1) Repository Layout (reference)

```

juicy-playbook-v1.0/
├─ .github/
│  └─ workflows/
│     ├─ build-pdf.yml            # builds PDF on push to main
│     ├─ release-upload.yml       # builds & attaches PDF on release
│     └─ changelog.yml            # auto-generates CHANGELOG on release
├─ docs/
│  ├─ Home.md                     # docs hub (Wiki alternative)
│  ├─ Development-Notes.md        # personal scratchpad
│  ├─ diagrams-notes.md
│  └─ runbooks.md
├─ status-api/
│  ├─ Dockerfile
│  └─ status\_api.py               # includes /api/status + new placeholders
├─ my-dashboard/
│  ├─ Dockerfile
│  └─ index.html                  # pinned Flight Hub, metrics, copy-to-URL
├─ pi/
│  └─ docker-compose.yml          # Pi services (HA, Mealie, ADS-B stack)
├─ scripts/
│  ├─ backup-server.sh
│  └─ verify-services.sh
├─ Juicy-Playbook-v1.0.md         # the playbook source
├─ Juicy-Playbook-v1.0.pdf        # generated PDF (also built by Actions)
├─ README.md
├─ .gitignore
└─ LICENSE

````

---

## 2) Working Model (how to make changes safely)

**Daily flow**
```bash
# 1) Do work on develop
git checkout develop
# edit files...
git add .
git commit -m "feat: your change"
git push

# 2) Open PR develop -> main and merge on GitHub when ready
# 3) Create release tag when you want a version (v1.1.1, v1.2.0...)
````

**Versioning (SemVer)**

*   **patch** `v1.1.1`: small fixes (label: `patch`)
*   **minor** `v1.2.0`: new features (labels: `minor`, `enhancement`)
*   **major** `v2.0.0`: breaking/large redesign (label: `major`)

***

## 3) GitHub Automation (what each workflow does)

### 3.1 Build PDF on Push (`.github/workflows/build-pdf.yml`)

*   Triggers on push to `main`.
*   Installs pandoc + `wkhtmltopdf`.
*   Builds `Juicy-Playbook-v1.0.pdf`.
*   Uploads as **Action artifact** (downloadable from Actions run).

### 3.2 Release Upload (`.github/workflows/release-upload.yml`)

*   Triggers when you **publish a release** (e.g., `v1.2.0`).
*   Builds the PDF and **attaches** it to the GitHub Release automatically.

### 3.3 Changelog Generator (`.github/workflows/changelog.yml`)

*   Triggers on **Release published**.
*   Generates/updates `CHANGELOG.md` and commits it.

**Where to see results**

*   **Actions** tab → latest run → **Artifacts** (for PDF built on push).
*   **Releases** tab → each release shows attached **PDF**.
*   Root repo → `CHANGELOG.md` auto‑committed on release.

***

## 4) Issues, Labels, Priorities, Milestones, Project Board

### 4.1 Labels you’re using now

*   Type/size: `major`, `minor`, `patch`, `enhancement`
*   Workflow: *(optional)* `ci`
*   Triage: `bug`, `documentation`, `question`
*   Priority: `P1`, `P2`, `P3`

### 4.2 Milestones

*   `v1.1.0` (current), `v1.2.0` (next), `v2.0.0` (major future)

### 4.3 Project board automations

*   New issues → **To Do**
*   Assigned → **In Progress**
*   Closed/Merged → **Done**

***

## 5) Status API — what’s live in source

**File:** `status-api/status_api.py` (already updated)

Endpoints:

*   `GET /api/status`  
    Returns service statuses (AMP, AI, Vault, Dashboard, Minecraft, Valheim, Ultrafeeder, FR24, FlightAware, RadarBox, HA, Mealie).

*   `GET /api/metrics` *(placeholder)*  
    Will expose CPU/RAM/Disk for host, CPU/RAM for Pi.

*   `GET /api/flight-summary` *(placeholder)*  
    Will expose aircraft count, MLAT state, and feeder health.

*   `GET /api/services` *(placeholder)*  
    Returns the set of known services (for UI scaffolding).

*   `GET /health`  
    Returns `'ok'` for container liveness.

> **When you’re back home** we’ll wire `/api/metrics` with `psutil` (host) and light Pi metrics, and `/api/flight-summary` from Ultrafeeder JSON.

***

## 6) Dashboard — what’s live in source

**File:** `my-dashboard/index.html` (already updated)

*   **Pinned Flight Hub** section with:
    *   “Open Flight Map” tile → `https://flights.jkeasy.com`
    *   Live **Aircraft** & **MLAT** if `/api/flight-summary` returns data
*   **Pi‑offline banner** if **all 4** flight feeders appear down  
    *(Ultrafeeder, FR24, FlightAware, RadarBox)*
*   **CPU/RAM mini bars** for Host and Pi if `/api/metrics` returns values
*   **Click‑to‑copy** on each tile copies the full URL
*   Groups services by **Flight Stack / Game Servers / Smart Home / AI / Apps / Management / Infrastructure / Security**
*   Refreshes every **10s** (graceful fallback if optional endpoints are missing)

***

## 7) DNS, Routing, and Certificates (when you’re home)

**Public IP (host):** `104.8.77.206`  
**Pi IP (LAN):** `192.168.1.73`

### 7.1 DNS (Squarespace or registrar)

Create **A** records pointing to host public IP:

    flights     A  104.8.77.206
    fr24        A  104.8.77.206
    piaware     A  104.8.77.206
    rb          A  104.8.77.206
    homeassistant  A  104.8.77.206
    mealie         A  104.8.77.206
    api            A  104.8.77.206
    dashboard      A  104.8.77.206
    amp            A  104.8.77.206
    vault          A  104.8.77.206
    ai             A  104.8.77.206

### 7.2 Traefik dynamic routes (host)

> If you manage Traefik via Coolify’s dynamic file, add a file like:

`/data/coolify/proxy/dynamic/juicypi-adsb.yml`

```yaml
http:
  routers:
    fr24:
      rule: "Host(`fr24.jkeasy.com`)"
      entrypoints: [https]
      tls: { certResolver: letsencrypt }
      service: fr24
    piaware:
      rule: "Host(`piaware.jkeasy.com`)"
      entrypoints: [https]
      tls: { certResolver: letsencrypt }
      service: piaware
    rb:
      rule: "Host(`rb.jkeasy.com`)"
      entrypoints: [https]
      tls: { certResolver: letsencrypt }
      service: rb
  services:
    fr24:
      loadBalancer:
        servers: [{ url: "http://192.168.1.73:8755" }]
    piaware:
      loadBalancer:
        servers: [{ url: "http://192.168.1.73:8081" }]
    rb:
      loadBalancer:
        # RB doesn't have a default UI; you can point to Ultrafeeder map for convenience
        servers: [{ url: "http://192.168.1.73:8080" }]
```

> Certificates: Traefik manages via `letsencrypt` (as in your labels/dynamic files).

***

## 8) Deploying containers (when you’re home)

> **Prereqs**: Docker installed on host; Docker network (e.g., `coolify`).

### 8.1 Status API (host)

```bash
ssh ampserver@104.8.77.206

# If repo is on the server:
cd ~/juicy-playbook-v1.0/status-api
git checkout main && git pull

# Build and run
docker build -t status-api .
docker rm -f status-api 2>/dev/null || true
docker run -d --name status-api --restart unless-stopped \
  --network coolify \
  -e JUICY_PUBLIC_IP=104.8.77.206 \
  -e JUICY_PI_IP=192.168.1.73 \
  -l "traefik.enable=true" \
  -l "traefik.http.routers.statusapi.rule=Host(`api.jkeasy.com`)" \
  -l "traefik.http.routers.statusapi.entrypoints=https" \
  -l "traefik.http.routers.statusapi.tls.certresolver=letsencrypt" \
  -l "traefik.http.services.statusapi.loadbalancer.server.port=5000" \
  status-api
```

**Smoke test**

```bash
curl -I https://api.jkeasy.com/health
curl -s https://api.jkeasy.com/api/status | jq '. | keys'
```

### 8.2 Dashboard (host)

```bash
ssh ampserver@104.8.77.206
cd ~/juicy-playbook-v1.0/my-dashboard
git checkout main && git pull

docker build -t juicy-dashboard .
docker rm -f juicy-dashboard 2>/dev/null || true
docker run -d --name juicy-dashboard --restart unless-stopped \
  --network coolify \
  -l "traefik.enable=true" \
  -l "traefik.http.routers.dashboard.rule=Host(`dashboard.jkeasy.com`)" \
  -l "traefik.http.routers.dashboard.entrypoints=https" \
  -l "traefik.http.routers.dashboard.tls.certresolver=letsencrypt" \
  -l "traefik.http.services.dashboard.loadbalancer.server.port=80" \
  juicy-dashboard
```

**Smoke test**

```bash
curl -I https://dashboard.jkeasy.com/
```

### 8.3 Pi services (LAN)

On the Pi:

```bash
ssh pi@192.168.1.73
cd ~/juicy-playbook-v1.0/pi
docker compose up -d
```

**Quick checks (from host)**

```bash
curl -I http://192.168.1.73:8080   # Ultrafeeder/tar1090
curl -I http://192.168.1.73:8081   # FlightAware (SkyAware)
curl -I http://192.168.1.73:8755   # FR24 web
# RB feeder is a TCP socket (30005) - use `nc -zv 192.168.1.73 30005`
```

***

## 9) Verification & Troubleshooting

**On host**

```bash
# container logs
docker logs --tail 50 status-api
docker logs --tail 50 juicy-dashboard

# reachability from host to Pi
curl -I http://192.168.1.73:8080
curl -I http://192.168.1.73:8081
curl -I http://192.168.1.73:8755
nc -zv 192.168.1.73 30005
```

**Common symptoms**

*   **Dashboard shows “Connecting…”** → `api.jkeasy.com` not reachable or `/api/status` failing
*   **Pi‑offline banner** → all four flight feeders down (`ultrafeeder`, `fr24`, `piaware`, `rbfeeder`)
*   **MLAT/Aircraft dashes** → `/api/flight-summary` still placeholder or feeder JSON not reachable
*   **CPU/RAM bars empty** → `/api/metrics` is placeholder (expected until implemented)

***

## 10) Security & Backups

*   **Never commit secrets** or `.env` files (your `.gitignore` already prevents typical leaks).
*   Use **Vaultwarden** for credentials.
*   **Backups**: run script or cron the `scripts/backup-server.sh` (tar configs, dynamic files, compose files).
*   **Rollback**: tag images you deploy (`status-api:YYYYMMDD`) and keep last known-good.

***

## 11) Implementing Real Metrics (later)

When back home:

**Host metrics** (Status API):

*   Add `psutil` to the image and implement `/api/metrics` to read CPU/RAM/Disk.

**Pi metrics**:

*   Option A: lightweight HTTP on Pi returning simple JSON.
*   Option B: SSH pull or MQTT messages.
*   Option C: expose `node_exporter` and scrape from host (heavier).

We’ll pick the simplest, low‑overhead option and wire the dashboard bars.

***

## 12) Release Checklist (future versions)

1.  Work on `develop` → PR → merge to `main`
2.  **Draft release** with tag `v1.2.0` (or `v1.1.1`)
3.  Release notes → **Publish**
4.  **Actions run**:
    *   Release upload attaches PDF
    *   Changelog workflow updates `CHANGELOG.md`
5.  Verify:
    *   Release page shows attached PDF
    *   `CHANGELOG.md` updated
    *   Board issues moved to **Done** by automation

***

## 13) Quick Copy/Paste Index

**Deploy Status API**

```bash
docker build -t status-api ./status-api
docker rm -f status-api 2>/dev/null || true
docker run -d --name status-api --restart unless-stopped \
  --network coolify \
  -e JUICY_PUBLIC_IP=104.8.77.206 \
  -e JUICY_PI_IP=192.168.1.73 \
  -l "traefik.enable=true" \
  -l "traefik.http.routers.statusapi.rule=Host(`api.jkeasy.com`)" \
  -l "traefik.http.routers.statusapi.entrypoints=https" \
  -l "traefik.http.routers.statusapi.tls.certresolver=letsencrypt" \
  -l "traefik.http.services.statusapi.loadbalancer.server.port=5000" \
  status-api
```

**Deploy Dashboard**

```bash
docker build -t juicy-dashboard ./my-dashboard
docker rm -f juicy-dashboard 2>/dev/null || true
docker run -d --name juicy-dashboard --restart unless-stopped \
  --network coolify \
  -l "traefik.enable=true" \
  -l "traefik.http.routers.dashboard.rule=Host(`dashboard.jkeasy.com`)" \
  -l "traefik.http.routers.dashboard.entrypoints=https" \
  -l "traefik.http.routers.dashboard.tls.certresolver=letsencrypt" \
  -l "traefik.http.services.dashboard.loadbalancer.server.port=80" \
  juicy-dashboard
```

**DNS** *(A records → 104.8.77.206)*  
`flights, fr24, piaware, rb, homeassistant, mealie, api, dashboard, amp, vault, ai`

***

## 14) What to do next (when you’re ready)

*   Implement real `/api/metrics` & `/api/flight-summary`.
*   Rebuild containers and verify dashboard bars & stats update.
*   Add **Uptime Kuma** monitors (`api.jkeasy.com/api/status`, `fr24/piaware/rb`, etc.).
*   Plan features for `v1.2.0` milestone; keep `v2.0.0` for big Flight Hub + redesign.

***

### End of Operational Guide

'@ | Set-Content -Encoding UTF8 docs\Operational-Guide.md

git add docs/Operational-Guide.md
git commit -m "docs: add Operational Guide (end-to-end setup & ops)"
git push

```

> If you prefer, I can also split this into smaller pages (Server Setup, Pi Setup, Flight Stack, Dashboard, Status API). Just say **“split docs”**.

Once you’ve saved it (UI or CLI), send me a quick **“Saved”**, and I’ll add a one‑line link in your README to this new guide so it’s easy to find.
```
