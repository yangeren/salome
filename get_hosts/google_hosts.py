#coding=utf-8
__author__ = 'Hanz'
from __init__ import *
from SendEmail import send_mail

def google_hosts():
    try:
        google_hosts_url = 'http://www.360kb.com/kb/2_122.html'
        res = requests.get(google_hosts_url).content   #取页面HTML内容
        soup = BeautifulSoup(res)
        con = soup.pre.string    #取HOSTS标签内容
        data = str(con)  #将beautifulsoup类型转为STR类型
        if 'google' not in data: print 'hahaah'
        f = open('google_hosts', 'w')   #写入文件备份
        f.writelines(data)
        f.close()

        m = open('google_hosts', 'r')   #只取IP地址
        hosts_list = list()
        for line in m.readlines()[11:]:
             hosts_list.append(line)
        # return hosts_list
        m.close()

        os.popen('copy C:\Windows\System32\drivers\etc\hosts C:\Windows\System32\drivers\etc\host.bak') #备份文件
        sys_hosts = open('C:\Windows\System32\drivers\etc\hosts','r')  #写入系统HOSTS文件
        hosts_start = '##############google get_hosts start#######################\n'
        sys_hosts_data = sys_hosts.readlines()
        lines = sys_hosts_data.index(hosts_start)  #取出标记位置
        all_hosts = sys_hosts_data[:lines + 1] + hosts_list  #hosts内容拼接
        sys_hosts.close()

        sys_hosts = open('C:\Windows\System32\drivers\etc\hosts','w')
        sys_hosts.write(''.join(all_hosts))  #写入
        sys_hosts.close()
        send_mail(content='seccess',subject=u'每日导入谷歌HOSTS日志')
    except Exception, e:
        send_mail(content=str(e),subject=u'每日导入谷歌HOSTS报错日志')



    # return con
google_hosts()
# a = google_hosts()
# print a

