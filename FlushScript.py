__author__ = 'yer'
#*--coding:utf-8--*
import re
import requests

def flush301(keyword):
    res = requests.get("http://www.zhongsou.net/%s" % keyword)
    res_data = res.content
    print res_data

if __name__=="__main__":
    flush301(u"小兔子乖乖")


