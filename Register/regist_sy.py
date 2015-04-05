#coding=utf-8
# __author__ = 'Hanz'
import requests
import random
import time


def reg(username):
    url = 'http://103.29.134.224/d3api2/user/register.groovy'
    # url = 'http://103.29.134.224/d3api2/user/register.groovy'
    data = {
        'vc': '3.0.0',
        'nick': username,
        'email': username+'@163.com',
        'password': '111111',
        'imei': random.randint(100000000000000,999999999999999),
        'name': username
    }
    print data
    req = requests.get(url,params=data)
    print req.content

for x in xrange(1,31):
    # member = 'whtest'+ str(x)
    # print member
    # reg(member)
    # time.sleep(5)
    member = 'zcs' + str(x).zfill(3)
    reg(member)
    time.sleep(5)
    # print member