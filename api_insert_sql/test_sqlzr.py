#*--coding:utf-8--*
import requests
import yaml

readyml = yaml.load(file('ini.yml'))
api_url = readyml['api']
sql = readyml['sql']
print sql
data = {
    'id': 'select * from sdfsf',
    'kw': '丛莱绿茶'
}
for x in api_url.split(' '):
    for y in sql.split(';'):
        data = {
            'id': '%s' % y,
            'kw': '丛莱绿茶'
        }
        res = requests.get(x, params=data)
        print y
        print res.url
        print res.status_code
        print res.content

