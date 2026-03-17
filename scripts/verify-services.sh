
#!/usr/bin/env bash
set -e
printf "
== Docker containers ==
"
docker ps --format "table {{.Names}}	{{.Status}}	{{.Ports}}"
printf "
== Traefik routes (curl checks) ==
"
for url in   https://dashboard.jkeasy.com   https://api.jkeasy.com/api/status   https://vault.jkeasy.com   https://ai.jkeasy.com
  do
  echo "- $url"; curl -fsSIL "$url" | head -n 1 || true; echo
done
