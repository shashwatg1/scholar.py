# http_proxy=http://10.3.100.207:8080
# https_proxy=https://10.3.100.207:8080
# export http_proxy
# export https_proxy
cd sch
(echo 'started on'
date | grep -o '..:..:..') > stat
(echo 'sleeping since'
date | grep -o '..:..:..'
echo 'sleeping for' $1) >> stat
sleep $1
# rm sleeping_now
export http_proxy=http://:@10.3.100.207:8080/
export https_proxy=https://:@10.3.100.207:8080/
g++ qToUrl.cpp
echo 'g++ done'
./a.out <qin >qout
mkdir 	HTML_scrapped
chmod +x wget_script.sh
echo 'running wget'
(echo 'working since'
date | grep -o '..:..:..') >> stat
python ssh_run.py
# rm working_now
(echo 'completed on'
date | grep -o '..:..:..') >> stat
(echo 'faults = '
grep -lr 'has moved' .
grep -lr 'has moved' . | wc -l ) >> stat
ls | grep '\.py' | xargs rm
ls | grep '\.cpp' | xargs rm
ls | grep '\.sh' | xargs rm
rm qout
rm a.out
rm cookie.txt
(echo 'Cleaning done'
echo 'total files = '
ls HTML_scrapped/ | wc -l
echo 'faults = '
grep -r -l 'The document has moved' HTML_scrapped/ | wc -l
) >> stat
(echo 'empty files = '
find . -type f -empty
find . -type f -empty -delete
echo 'finished') >>stat
cp -f stat ../
# scp -r /home/user/sch/HTML_scrapped us