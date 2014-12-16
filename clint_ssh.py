
import paramiko
import threading
def ssh2(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            out = stdout.readlines()
            for o in out:
                print o,
        print '%s\tOK\n'%(ip)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)
	ssh.close()
if __name__=='__main__':
    # cmd = ['pwd','cal','echo hello!']
    cmd = ['pwd','cd /usr/local/tomcat/webapps/np/WEB-INF/classes','ll redirectkeywordbyhost.txt']
    mall_id = str(raw_input())
    # cmd = ['cal','pwd','cd /zsimage/b2bnews/blog%s;tar -czvf %s.tar.gz %s/'%(mall_id[-3:],mall_id,mall_id),'pwd']
    print cmd
    username = "wending"
    passwd = "NetDIsk*_3&j"
    threads = []
    print "Begin......"
    clint_ip = [
#	'202.108.1.121',
	'202.108.1.122',
#	'202.108.33.224',
#       '202.108.33.233',
#       '202.108.33.171',
#       '202.108.33.176',
#       '103.29.134.108',
#       '103.29.134.109'
	]
    for i in clint_ip:
        # ip = '202.108.33.'+str(i)
        a=threading.Thread(target=ssh2,args=(i,username,passwd,cmd))
        a.start()
