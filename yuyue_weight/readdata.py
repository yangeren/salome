__author__ = 'hanz'
#*-- coding=utf-8 --*
import yaml
class ReadData(object):
    def readdata(self, user):
        res = yaml.load(file('ini.yaml'))
        login_url = res['url']['login']
        username = res[user]['username']
        password = res[user]['password']
        xuanchuantu = res['road']['xuanchuantu']
        print username,password
        return login_url, username, password, xuanchuantu