import os
import tempfile
import sys
import pexpect
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

def scp(destination, file_id, user, password, timeout=30, bg_run=False):
    """SSH'es to a host using the supplied credentials and executes a command.
    Throws an exception if the command doesn't return 0.
    bgrun: run command in the background"""

    fname = tempfile.mktemp()
    fout = open(fname, 'w')

    options = '-q -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -oPubkeyAuthentication=no'
    if bg_run:
        options += ' -f'
    ssh_cmd = 'scp %s %s' % (file_id, destination)
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





with open('run.sh', 'r') as myfile:
	data=myfile.read().replace('\n', ';')
print data
with open('IPs', 'r') as myfile:
	ips=myfile.read().splitlines()
j = 1
file_id2 = '/home/cj41018/Desktop/qToUrl.cpp'
file_id3 = '/home/cj41018/Desktop/wget_script.sh'
file_id4 = '/home/cj41018/Desktop/ssh_run.py'
for ip in ips:
    try:
		qin_name = 'qin'+str(j)+ '/qin'
		file_id = '/home/cj41018/Desktop/' + qin_name
		destination = 'user@' + ip + ':/home/user/sch'
		print 'B'
		print ssh(ip, 'mkdir sch;', 'user', 'user12')
		print 'B'
		print scp(destination, file_id, 'user', 'user12')
		print 'B'
		print scp(destination, file_id2, 'user', 'user12')
		print 'B'
		print scp(destination, file_id3, 'user', 'user12')
		print 'B'
		print scp(destination, file_id4, 'user', 'user12')
		print 'B'
		print ssh(ip, data, 'user', 'user12')
		print 'B'
		j+=1	
    except:
		print 'errored'
