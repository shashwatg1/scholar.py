import os
import tempfile
import sys
import time
import pexpect
def ssh(host, cmd, user, password, timeout=30, bg_run=False):
    """SSH'es to a host using the supplied credentials and executes a command.
    Throws an exception if the command doesn't return 0.
    bgrun: run command in the background"""

    # return ''
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

def ssh_detached(host, cmd, user, password, timeout=30, bg_run=False):
    """SSH'es to a host using the supplied credentials and executes a command.
    Throws an exception if the command doesn't return 0.
    bgrun: run command in the background"""

    fname = tempfile.mktemp()
    fout = open(fname, 'w')

    options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
    if bg_run:
        options += ' -f'
    ssh_cmd = 'ssh %s@%s %s screen -d -m "%s"' % (user, host, options, cmd)
    print ssh_cmd
    # return ''
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

def scp(destination, file_id, user, password, timeout=30, bg_run=False):
    """SSH'es to a host using the supplied credentials and executes a command.
    Throws an exception if the command doesn't return 0.
    bgrun: run command in the background"""

    fname = tempfile.mktemp()
    fout = open(fname, 'w')

    options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
    if bg_run:
        options += ' -f'
    ssh_cmd = 'scp %s %s %s' % (options, file_id, destination)
    print ssh_cmd
    # return ''
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





# with open('run.sh', 'r') as myfile:
	# data=myfile.read().replace('\n', ';')
data = 'bash ~/sch/run.sh'
# qinlist = '/home/user/sch/Abhinav/qinlist'
with open('qinlist', 'r') as myfile:
    qinlist = myfile.read().splitlines()
print data
with open('IPs', 'r') as myfile:
	ips=myfile.read().splitlines()
j = 1
file_id2 = '/home/user/Desktop/sch/Abhinav/qToUrl.cpp'
file_id3 = '/home/user/Desktop/sch/Abhinav/wget_script.sh'
file_id4 = '/home/user/Desktop/sch/Abhinav/ssh_run.py'
file_id5 = '/home/user/Desktop/sch/Abhinav/run.sh'
xk = 0
err = []
for ip in ips:
	if len(ip) <=2:
		continue
	try:
		file_id = '/home/user/Desktop/sch/Abhinav/' + qinlist[j-1]
		print 'j = ', j, 'qin = ', qinlist[j-1]
		j+=1
		destination = 'user@' + ip + ':~/sch/'
		print 'B'
		try:
			print ssh(ip, 'rm -rf sch', 'user', 'user12')
			print 'B-'
		except: pass
		print ssh(ip, 'mkdir sch;', 'user', 'user12')
		print 'mkdir'
		time.sleep(0.4)
		print scp(destination, file_id2, 'user', 'user12')
		print 'file_id2'
		time.sleep(0.4)
		print scp(destination+'qin', file_id, 'user', 'user12')
		print 'file_id'
		time.sleep(0.4)
		print scp(destination, file_id3, 'user', 'user12')
		print 'file_id3'
		time.sleep(0.4)
		print scp(destination, file_id4, 'user', 'user12')
		print 'file_id4'
		time.sleep(0.4)
		print scp(destination, file_id5, 'user', 'user12')
		print 'file_id5'
		time.sleep(3);
		waitt = ' '+str(int(xk*8+2*xk**1.37+0.65*xk**1.77))+'m'
		print >> sys.stderr, ip + ' '+file_id+' ' + waitt
		xk += 1
		print ssh_detached(ip, data+waitt, 'user', 'user12')

		print 'data'
	except:
		j-=1
		err.append(ip)
		print 'errored'
		pass

print 'error in: '
print err
if len(qinlist) - j > 0:
    print 'can\'t last process ' +str(len(qinlist) - j) + 'files'