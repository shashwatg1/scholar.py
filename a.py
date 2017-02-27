import os
import tempfile
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

with open('run.sh', 'r') as myfile:
        data=myfile.read().replace('\n', ';')
print data
ip_string = '10.5.16.'
for ip_end in range(1000):
    ip = ip_string + str(ip_end)
    try:
        print ssh(ip, data, 'user', 'user12')
    except:
        print 'errored'
