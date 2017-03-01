echo 'getting ip it may take some time'
nmap -Pn 10.5.16.1/24 2>&1 | tee ipp
echo 'done'
pcregrep -M 'Nmap.*\n.*\n.*\n.*\n.*ssh' ipp  | grep -o '10\.5.*' > ip

echo 'Total ssh active hosts = '
cat ip  | wc -l 