__author__ = 'yer'
#*--coding:utf-8--*
import re
import requests
import yaml
power_dict = []
keyword_dict = []
pageid_dict = []
ig_id_dict = []
def flush301(keywords):
    menhu = {}

    try:
        res = requests.get("http://www.zhongsou.net/%s" % keywords)
        res_data = res.content
        power = re.findall(r'g_widgetSerial=".*"', res_data)[0]
        keyword =  re.findall(r'g_keyword = ".*"', res_data)[0]
        pageid =  re.findall(r'g_curPageNum = .*;', res_data)[0]
        ig_id =  re.findall(r'g_owner=".*"', res_data)[0]
        # print res_data
        # print power,keyword,pageid,ig_id
        # power_dict.append(power.split('"')[1])
        # print power_dict
        # print power.split('"')[1]
        # print keyword.split('"')[1]
        # print pageid.split(' ')[2][0:-1]
        # print ig_id.split('"')[1]
        # print "------------------"
        power_dict = (power.split('"')[1])
        keyword_dict = (keyword.split('"')[1])
        pageid_dict = (pageid.split(' ')[2][0:-1])
        ig_id_dict = (ig_id.split('"')[1])
        print power_dict, keyword_dict, pageid_dict, ig_id_dict
    except:
        print u"没有这个门户词：" + keywords


    # print "keyword:"+keyword
    # print "pageid:"+pageid
    # print "ig_id:"+ig_id

def readyml():
    s = yaml.load(file('keyword.yml'))
    a = s['keyword'].split(' ')
    # print a
    # print a.split(' ')
    # for x in a.split(' '):
    #     print x
    # print type(a)
    # print type(s['host']['ip01'])
    return a


if __name__=="__main__":
    # keywords = raw_input("请输入门户词：\n")
    # k = readyml()
    # print k
    # a = []
    # b = []
    # c = []
    # d = []
    for x in readyml():
        # print x
        flush301(x)

    # readyml()


