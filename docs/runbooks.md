
# Runbooks (Ops)

## API down
1) `docker logs status-api --tail 50`
2) `docker restart status-api`
3) Check DNS for `api.jkeasy.com` and Traefik labels.

## Port conflict on 5000/8080
- Find listener: `sudo ss -tulpn | grep -E ':5000|:8080'`
- Stop conflicting process, then `docker rm -f <name>` and recreate.

## AMP login reset
`sudo -u amp ampinstmgr --ResetLogin ADS01 admin "<NEW PASS>"`

## Pi unresponsive
- HA → Smart plug power‑cycle
- Or physical reboot

## Mealie not responding on 9090
- Ensure mapping `9090:9000`
- `docker logs mealie --tail 50`
- Remove and recreate container if needed
