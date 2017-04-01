import os
import time
import random
import sys
import tempfile
import pexpect
k = 0
myip='10.5.16.240'
with open('qin', 'r') as myfile:
	querries=myfile.read().splitlines()

with open('qout', 'r') as myfile:
	urls=myfile.read().splitlines()
waited_once = 0;
xk = 0
for i in range(len(urls)):
	querries[i]=querries[i].replace(' ','_')
	if querries[i] < 3:
		continue
	print 'running: ' + 'bash wget_script.sh ' + urls[i] + ' ' + 'HTML_scrapped/' + querries[i]
	x = os.popen('bash wget_script.sh \'' + urls[i] + '\' ' + 'HTML_scrapped/' + querries[i] + '&>> log.txt')
	ran = int(36+24*xk**0.5 + 10*xk**0.3);
	time.sleep(int(ran/3+3*xk+random.randint(ran/4,ran/2)))
	xk += 1
	if 'wget failed' in x:
		os.popen('rm HTML_scrapped/' + querries[i])
		k +=1
	else:
		k=0
	if k==3:
		sys.exit()
	if not waited_once: # if moved wait for 30min and then go ahead
		try:
			x = os.popen("grep -r -l 'The document has moved' . > fault")
			with open('fault', 'r') as f:
				x = f.read()
			if x.count('The document has moved') >= 4:
				os.popen("(echo 'waiting since'; date) >> waiting")
				os.system("sleep 30m")
				os.popen("(echo 'waited till'; date) >> waiting")
				os.system("rm cookie.txt")
				waited_once = 1
		except:
			waited_once = 1
			pass

def ssh(host, cmd, user, password, timeout=30, bg_run=False):
	"""SSH'es to a host using the supplied credentials and executes a command.
	Throws an exception if the command doesn't return 0.
	bgrun: run command in the background"""

	fname = tempfile.mktemp()
	fout = open(fname, 'w')

	options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
	if bg_run:
		options += ' -f'
	ssh_cmd = 'ssh %s@%s %s "%s"' % (user, host, options, cmd)
	child = pexpect.spawn(ssh_cmd, timeout=timeout)
	child.expect(['password: '])
	child.sendline(password)
	child.logfile = fout
	child.expect(pexpect.EOF)
	child.close()
	fout.close()

	fin = open(fname, 'r')
	stdout = fin.read()
	fin.close()

	if 0 != child.exitstatus:
		raise Exception(stdout)

	return stdout

def scpr(destination, file_id, user, password, timeout=30, bg_run=False):
	"""SSH'es to a host using the supplied credentials and executes a command.
	Throws an exception if the command doesn't return 0.
	bgrun: run command in the background"""

	fname = tempfile.mktemp()
	fout = open(fname, 'w')

	options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
	if bg_run:
		options += ' -f'
	ssh_cmd = 'scp -r %s %s %s' % (options,file_id, destination)
	print ssh_cmd
	child = pexpect.spawn(ssh_cmd, timeout=timeout)
	child.expect(['password: '])
	child.sendline(password)
	child.logfile = fout
	child.expect(pexpect.EOF)
	child.close()
	fout.close()

	fin = open(fname, 'r')
	stdout = fin.read()
	fin.close()

	if 0 != child.exitstatus:
		raise Exception(stdout)


	return stdout
sr1 = querries[0]+str(random.randint(1,99))
sr2 = querries[0]+str(random.randint(1,99))
try:
	myip = '10.5.16.230'
	scpr('user@'+myip+':~/saves/'+sr1, 'HTML_scrapped', 'user', 'user12')
	time.sleep(2)
	myip = '10.5.16.42'
	scpr('user@'+myip+':~/saves/'+sr1, 'HTML_scrapped', 'user', 'user12')
	time.sleep(2)
	myip = '10.5.16.101'
	scpr('user@'+myip+':~/saves/'+sr1, 'HTML_scrapped', 'user', 'user12')
	time.sleep(2)
	# myip = '10.5.16.230'
	# scpr('user@'+myip+':~/saves/'+sr1, 'HTML_scrapped', 'user', 'user12')

except:
	time.sleep(2)
	try:

		myip = '10.5.16.42'
		scpr('user@'+myip+':~/saves/'+sr1, 'HTML_scrapped', 'user', 'user12')
		scpr('user@'+myip+':~/saves/'+sr2, 'HTML_scrapped', 'user', 'user12')
		myip2='10.5.16.230'
		scpr('user@'+myip2+':~/saves/'+sr2, 'HTML_scrapped', 'user', 'user12')
		myip3 = '10.5.16.42'
		scpr('user@'+myip3+':~/saves/'+sr2, 'HTML_scrapped', 'user', 'user12')
	except:

		myip = '10.5.16.101'
		scpr('user@'+myip+':~/saves/'+sr1, 'HTML_scrapped', 'user', 'user12')
		print 'scpr has errored'
		f = open('error', 'and')
		f.write('scpr has errored')
		f.write('user@'+myip+':~/saves/'+sr2+'\n')
		# f.write('user@'+myip+':~/saves/'+sr2+)
		f.close()