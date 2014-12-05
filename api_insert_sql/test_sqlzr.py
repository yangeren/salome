#*--coding:utf-8--*
import requests
import yaml
import json

readyml = yaml.load(file('ini.yml'))
api_url = readyml['api']
sql = readyml['sql']
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
            print(res_get.history,res_post.history)
            if res_get.url != 'http://202.108.1.121/403.html':
            # if res_get.status_code == 500:
                m += 1
                print(y)
                print(res_get.url)
                print(res_get.status_code)

            if res_post.url != 'http://202.108.1.121/403.html':
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
