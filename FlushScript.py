__author__ = 'yer'
#*--coding:utf-8--*
import re
import requests
import yaml
import json

def flush301(keywords, ip, flushurl):
    try:
        res = requests.get("http://www.zhongsou.net/%s" % keywords)
        res_data = res.content
        powerstr = re.findall(r'g_widgetSerial=".*"', res_data)[0]
        keyword =  re.findall(r'g_keyword = ".*"', res_data)[0]
        pageid =  re.findall(r'g_curPageNum = .*;', res_data)[0]
        ig_id =  re.findall(r'g_owner=".*"', res_data)[0]
        power_dict = (powerstr.split('"')[1])
        keyword_dict = (keyword.split('"')[1])
        pageid_dict = (pageid.split(' ')[2][0:-1])
        ig_id_dict = (ig_id.split('"')[1])
        print keyword_dict, ig_id_dict, pageid_dict, power_dict
        for x in ip:
            data = {
                "ip" : x,
                "port" : 2047,
                "jsonStr" : "",
                "pr" : "",
                "pageid" : pageid_dict,
                "press" : "ok"
            }
        po = requests.post(flushurl, data=json.dumps(data))
        # po = requests.post(flush_url, data=ss)
        # print po.content
    except:
        print u"没有这个门户词：" + keywords

def readyml():
    readres = yaml.load(file('keyword.yml'))
    keyword = readres['keyword'].split(' ')
    np = readres['ip']['nginx'].split(' ')
    pageflush = readres['url']['b2b']['pageflush']
    ipflush = readres['url']['b2b']['ipflush'].split(' ')
    return keyword, np, pageflush, ipflush


if __name__=="__main__":
    keyword, np, pageflush, ipflush = readyml()
    for x in keyword:
        flush301(x, ipflush, pageflush)


