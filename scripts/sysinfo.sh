#!/bin/bash
echo "Current user:"
whoami

echo "Current date:"
date

echo "Disk usage:"
df -h

chmod +x scripts/sysinfo.sh
./scripts/sysinfo.sh