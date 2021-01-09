#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

SCRIPTDIR=$(dirname $(readlink -f $0))

# get version from _version.py
VERSION_LINE=$(sed "3q;d" bettersis/_version.py)
read -ra version_arr -d '' <<<"$VERSION_LINE"
VERSION=${version_arr[3]//\"}

CONTROL_PATH=build/bettersis/DEBIAN/control
POSTINST_PATH=build/bettersis/DEBIAN/postinst

if [ $# -ne 0 ] ; then
    # if on vagrant VM, copy the folder to prevent chmod problems
    cp -r /etc/synced_folder $HOME/.
    SCRIPTDIR=$HOME/synced_folder
fi

# -- Make bettersis executable using Pyinstaller
echo ""
echo "-------------------------------------------"
echo ""
echo "MAKE EXECUTABLE USING PYINSTALLER"
echo ""
cd $SCRIPTDIR/bettersis
python3 -m PyInstaller bettersis.py --onefile -y --clean
cd ..

# -- Get executable size
echo ""
echo "-------------------------------------------"
echo ""
echo "GET EXECUTABLE SIZE"
echo ""
FILENAME=$SCRIPTDIR/bettersis/dist/bettersis
BYTE_FILESIZE=$(stat -c%s $FILENAME)
FILESIZE=$(bc -l <<< "scale = 0; $BYTE_FILESIZE / 1024")

echo "[DEBUG] FILESIZE: $FILESIZE"
echo "[DEBUG] BYTE_FILESIZE: $BYTE_FILESIZE"
echo "[DEBUG] CHECKSUM_SHA1: $CHECKSUM_SHA1"

# -- Make bettersis debian package
echo ""
echo "-------------------------------------------"
echo ""
echo "MAKE DEBIAN .deb PACKAGE"
echo ""
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

# create the postinst script that creates the syslog config file to also save the logs inside the /var/log/pybettersis.log file
# then restart rsyslog to commit the configuration
echo "#!/usr/bin/env bash" > $POSTINST_PATH
echo "echo ':programname, startswith, \"bettersis\", -/var/log/pybettersis.log' > /etc/rsyslog.d/24-pybettersis.conf" >> $POSTINST_PATH
echo "echo '& ~' >> /etc/rsyslog.d/24-pybettersis.conf" >> $POSTINST_PATH
echo "sudo service rsyslog restart" >> $POSTINST_PATH

cp $FILENAME $SCRIPTDIR/build/bettersis/usr/bin/bsis

cd $SCRIPTDIR/build
chmod -R 755 bettersis

dpkg --build bettersis

cp bettersis.deb ..
cd ..

if [ $# -ne 0 ] ; then
    # if on vagrant VM, copy the build outputs to the synced_folder folder
    cp $HOME/synced_folder/bettersis.deb /etc/synced_folder/.
    cp $HOME/synced_folder/bettersis/dist/bettersis /etc/synced_folder/bsis
fi