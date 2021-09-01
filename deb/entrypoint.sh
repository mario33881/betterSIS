#!/usr/bin/env bash
set -euo pipefail
set -x
IFS=$'\n\t'

cd /src/deb
chmod +x ./build.sh
./build.sh
