__author__ = 'yer'
#*--coding:utf-8--*
import re
import requests
import yaml

def flush301(keywords):
    res = requests.get("http://www.zhongsou.net/%s" % keywords)
    res_data = res.content
    keyword =  re.findall(r'g_keyword = ".*"', res_data)[0]
    pageid =  re.findall(r'g_curPageNum = .*;', res_data)[0]
    ig_id =  re.findall(r'g_owner=".*"', res_data)[0]
    # print res_data
    print keyword,pageid,ig_id
    print keyword.split('"')[1]
    print pageid.split(' ')[2][0:-1]
    print ig_id.split('"')[1]
    # print "keyword:"+keyword
    # print "pageid:"+pageid
    # print "ig_id:"+ig_id

def readyml():
    s = yaml.load(file('keyword.yml'))
    a = s['keyword']
    print a
    print a.split(' ')
    for x in a.split(' '):
        print x
    print type(a)
    print type(s['host']['ip01'])


if __name__=="__main__":
    # keywords = raw_input("请输入门户词：\n")
    # flush301(keywords)
    readyml()


