#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

SCRIPTDIR=$(dirname $(realpath $0))

VERSION=1.0.0
CONTROL_PATH=build/bettersis/DEBIAN/control

# -- Make bettersis executable using Pyinstaller
cd $SCRIPTDIR/bettersis
pyinstaller bettersis.py --onefile
cd ..

# -- Get executable size and checksum
FILENAME=$SCRIPTDIR/bettersis/dist/bettersis
BYTE_FILESIZE=$(stat -c%s $FILENAME)
FILESIZE=$(bc -l <<< "scale = 0; $BYTE_FILESIZE / 1024")
CHECKSUM_SHA1=$(sha1sum $FILENAME | awk '{ print $1 }')
echo "[DEBUG] FILESIZE: $FILESIZE"

# -- Make bettersis debian package
mkdir -p $SCRIPTDIR/build/bettersis/DEBIAN
mkdir -p $SCRIPTDIR/build/bettersis/usr/bin

echo "Package: bettersis" > $CONTROL_PATH
echo "Version: $VERSION" >> $CONTROL_PATH
echo "Section: custom" >> $CONTROL_PATH
echo "Priority: optional" >> $CONTROL_PATH
echo "Architecture: all" >> $CONTROL_PATH
echo "Essential: no" >> $CONTROL_PATH
echo "Installed-Size: $FILESIZE" >> $CONTROL_PATH
echo "Maintainer: Zenaro Stefano" >> $CONTROL_PATH
echo "Description: Improved interactive shell for SIS" >> $CONTROL_PATH
echo "Homepage: https://github.com/mario33881/bettersis" >> $CONTROL_PATH
echo "Checksums-Sha1:" >> $CONTROL_PATH
echo " $CHECKSUM_SHA1 $BYTE_FILESIZE bsis" >> $CONTROL_PATH

cp $FILENAME $SCRIPTDIR/build/bettersis/usr/bin/bsis

cd $SCRIPTDIR/build
chmod -R 755 bettersis

dpkg-deb --build bettersis

cp bettersis.deb ..
cd ..