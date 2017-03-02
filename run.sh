http_proxy=http://10.3.100.207:8080
https_proxy=https://10.3.100.207:8080
export http_proxy
export https_proxy

cd sch
g++ qToUrl.cpp
echo 'g++ done'
./a.out <qin >qout
mkdir 	HTML_scrapped
chmod +x wget_script.sh
echo 'running wget'
python ssh_run.py
