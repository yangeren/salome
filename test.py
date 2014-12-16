#*--coding:utf-8--*
__author__ = 'yer'
import yaml
import requests

document = """
  a: 1
  b:
    c: 3
    d: 4
"""
# print yaml.dump(yaml.load(document))

# p = yaml.load(file('/home/hanz/PycharmProjects/salome/Flush/keyword.yml'))
# a = p['soft']
# b = p['member']
# print b.items()
# for m, n in b.items():
#     print m
#     print n
# print a
# print b
# print a.items()
# for x,y in a.items():
#     print x,y

def comment(content, token, id, interest_id):
    pl_url = 'http://api2.souyue.mobi/d3api2/interest/blog.save.groovy?vc=4.0.2'
    data = {
        "blog_id": "0",
        "content": content,
        "mblog_id": id,
        "token": token,
        "user_ids": "",
        "interest_id": interest_id,
        "title": ""
    }
    headers = {'User-Agent': '中搜搜悦 4.0.2 (iPhone; iPhone OS 8.1; zh_CN)'}
    print data
    # pl = requests.post(pl_url, data=data, headers=headers)
    pl = requests.get(pl_url, params=data)
    print pl.content

if __name__=="__main__":
    comment(u'真心是好东西', '5e76493c-a698-48a6-8382-6e994fd47d3e', '1102077', '68')