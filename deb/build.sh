#!/usr/bin/env bash
set -euo pipefail
set -x
IFS=$'\n\t'

SCRIPTDIR=$(dirname $(readlink -f $0))

# get version from _version.py
VERSION_LINE=$(sed "3q;d" $SCRIPTDIR/../bettersis/_version.py)
IFS=' ' read -r -a version_arr <<< "$VERSION_LINE"
VERSION=${version_arr[3]//\"}

CONTROL_PATH=$SCRIPTDIR/build_area/bettersis/DEBIAN/control
POSTINST_PATH=$SCRIPTDIR/build_area/bettersis/DEBIAN/postinst

ls $CONTROL_PATH
# -- Get executable size
echo ""
echo "-------------------------------------------"
echo ""
echo "GET EXECUTABLE SIZE"
echo ""
FILENAME=$SCRIPTDIR/../dist/linux/bettersis
BYTE_FILESIZE=$(stat -c%s $FILENAME)
FILESIZE=$(bc -l <<< "scale = 0; $BYTE_FILESIZE / 1024")

echo "[DEBUG] FILESIZE: $FILESIZE"
echo "[DEBUG] BYTE_FILESIZE: $BYTE_FILESIZE"

# -- Make bettersis debian package
echo ""
echo "-------------------------------------------"
echo ""
echo "MAKE DEBIAN .deb PACKAGE"
echo ""

rm -rf $SCRIPTDIR/build_area/bettersis/usr/bin/executable_here
echo "Version: $VERSION" >> $CONTROL_PATH
echo "Installed-Size: $FILESIZE" >> $CONTROL_PATH

cp $FILENAME $SCRIPTDIR/build_area/bettersis/usr/bin/bsis

cd $SCRIPTDIR/build_area
ls
chmod -R 755 bettersis

dpkg --build bettersis

cp bettersis.deb ..
cd ..

pwd
ls
