import os
import time
import random
import sys
k = 0
with open('/home/user/sch/qin', 'r') as myfile:
	querries=myfile.read().splitlines()

with open('/home/user/sch/qout', 'r') as myfile:
	urls=myfile.read().splitlines()

for i in range(len(urls)):
	querries[i]=querries[i].replace(' ','')
	print 'running: ' + 'bash /home/user/sch/wget_script.sh ' + urls[i] + ' ' + '/home/user/sch/HTML_scrapped/' + querries[i]
	x = os.popen('bash /home/user/sch/wget_script.sh ' + urls[i] + ' ' + '/home/user/sch/HTML_scrapped/' + querries[i])
	time.sleep(6+random.randint(6,14))
	if 'wget failed' in x:
		os.popen('rm /home/user/sch/HTML_scrapped/' + querries[i])
		k +=1
	else:
		k=0
	if k==3:
		sys.exit()
