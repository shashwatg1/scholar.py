
ROOTUID="0"

if [ "$(id -u)" -ne "$ROOTUID" ] ; then
    echo "This script must be executed with root privileges."
    echo "use sudo :P -Abhinav"
    exit 1
fi

echo 'getting ip. it may take some time'
nmap -sS -p 22 10.5.16.1/24 > ipp
cat ipp
echo 'done'
cat  ipp  | grep -o '10\.5.*' > ip

echo 'Total ssh active hosts = '
cat ip  | wc -l 