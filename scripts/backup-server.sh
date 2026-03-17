
#!/usr/bin/env bash
set -euo pipefail
DST="/mnt/backup/juicy-$(date +%Y%m%d)"
sudo mkdir -p "$DST"
sudo tar czf "$DST/etc.tar.gz" /etc
sudo tar czf "$DST/docker-volumes.tar.gz" /var/lib/docker/volumes
sudo tar czf "$DST/amp.tar.gz" /home/amp/.ampdata || true
sudo -u $USER tar czf "$DST/home-$USER.tar.gz" "/home/$USER"
dpkg --get-selections > "$DST/packages.txt"
echo "Backup done at $DST"
