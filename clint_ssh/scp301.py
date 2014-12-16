__author__ = 'hanz'
#*--coding=utf-8--*
import paramiko
import threading

def scpfile(ip, username, passwd, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=10)
        for x in cmd:
            stdin, stdout, stderr = ssh.exec_command(x)
            print x
            out = stdout.readlines()
            for o in out:
                print o,
        print '%s\tOK'%(ip)
        ssh.close()
    except:
        print '%s\tError\n'%(ip)
    ssh.close()

if __name__=='__main__':
    cmd = ['pwd','cd /usr/local/tomcat/webapps/np/WEB-INF/classes','ll redirectkeywordbyhost.txt']
    print cmd
    username = 'wending'
    passwd = 'NetDIsk*_3&j'
    threads = []
    print "Begin........"
    clint_ip = [
        '202.108.1.122',
        # '202.108.33.224',
        # '202.108.33.233',
        # '202.108.33.171',
        # '202.108.33.176',
        # '103.29.134.108',
        # '103.29.134.109'
    ]
    for i in clint_ip:
        a = threading.Thread(target=scpfile, args=(i, username, passwd, cmd))
        a.start()