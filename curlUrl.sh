#!/bin/sh

url=$1
out_file=$2
# This code will get the source of the given Url
# To execute:
# chmod 755 curlUrl.sh
# ./curlUrl.sh > out

useragent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0"
#url="http://www.google.co.in/"

curl -A $useragent --cookie cookies.txt --cookie-jar cookie.txt --connect-timeout 10 $url > $out_file
