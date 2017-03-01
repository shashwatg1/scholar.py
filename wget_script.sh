#!/bin/sh

url=$1
out_file=$2
useragent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0'
# echo $useragent
# wget  http://wiki.bash-hackers.org/syntax/quoting --timeout 8 --user-agent="$useragent"
cookiefile='cookie.txt'
wget -q --user-agent="$useragent" -O  $out_file $url --timeout 8 --waitretry=3 --load-cookies $cookiefile --keep-session-cookies --save-cookies $cookiefile -t 2 
# # wget --header="Accept: text/html" --user-agent=$useragent -O $out_file --timeout 8 --waitretry=3 --load-cookies $cookiefile --keep-session-cookies --save-cookies $cookiefile -t 2 $url
if [[ $? -ne 0 ]]; then
    echo "wget failed"
    exit 1; 
else echo "wget success"
    exit 0;
fi
