# coding=utf-8
__author__ = 'yer'
import re
import requests
import yaml
import json


def flush301(keywords, ip, flushurl):
    try:
        res = requests.get("http://www.zhongsou.net/%s" % keywords)
        # res = requests.get("http://"+keywords, timeout=10)
        res_data = res.content
        powerstr = re.findall(r'g_widgetSerial=".*"', res_data)[0]
        keyword = re.findall(r'g_keyword = ".*"', res_data)[0]
        pageid = re.findall(r'g_curPageNum = .*;', res_data)[0]
        ig_id = re.findall(r'g_owner=".*"', res_data)[0]
        domain = re.findall(r'g_syshost=".*";', res_data)[0]
        power_dict = (powerstr.split('"')[1])
        keyword_dict = (keyword.split('"')[1])
        pageid_dict = (pageid.split(' ')[2][0:-1])
        ig_id_dict = (ig_id.split('"')[1])
        # domain_dict = (domain.split("")[1])
        flushjingtaiye = 'http://www.zhongsou.net/np/igdc?action=pagerelease&keyword=%s&pageid=%s' % (
            keyword_dict, pageid_dict)
        flushjingtaiye_data = requests.get(flushjingtaiye)
        print '----------**********----------'
        print flushjingtaiye_data.url
        print '|' + keyword_dict, ig_id_dict, pageid_dict, domain, power_dict
        for x in ip:
            data = {
                "ip": x,
                "port": 2047,
                "jsonStr": '',
                "pr": '',
                "pageid": pageid_dict,
                #"press" : "ok"
            }
            # print data
            po = requests.post(flushurl, data=data)
            # po = requests.get(flushurl, params=data)
            print u"|%s刷新静态页:   " % x + str(po.status_code)
        print '------------------------------'
        #print po.url
        # po = requests.post(flush_url, data=ss)
        # print po.content
    except Exception, e:
        print u"没有这个门户词：" + keywords, e


def fluship(ipflush):
    for m in ipflush:
        requests.get(m)
        print u"IP地址刷新成功：" + m
    print '------------------------------'


def readyml():
    # for liunx path
    # readres = yaml.load(file('/home/hanz/PycharmProjects/salome/Flush/keyword.yml'))
    # for windows path
    readres = yaml.load(file('D:\PycharmProjects\salome\Flush\keyword.yml'))
    keyword = readres['keyword'].split(' ')
    np = readres['ip']['nginx'].split(' ')
    pageflush = readres['url']['b2b']['pageflush']
    ipflush = readres['url']['b2b']['ipflush'].split(' ')
    domainflush = readres['url']['needflush'].split(' ')
    return keyword, np, pageflush, ipflush, domainflush


def flushdomain(domainflush):
    for x in domainflush:
        flushmemcache = 'http://202.108.1.122/np/getKeyword?url=%s' % x

        #此接口需要清两次域名，一次带www的，一次不带www的。
        flushurl = 'http://202.108.1.122/space/testmemcache.php?url=kwByDomain_%s&type=1' % x
        s = requests.get(flushurl)
        m = requests.get(flushmemcache)
        try:
            aa = requests.get("http://" + x, timeout=10)
            if 'http://image.zhongsou.com/image/notenew.gif' not in aa.content:
                print x
        except:
            print "timeout"

            # print x
            # print m.content
            # print s.content
            # if "?xml" in s.content:
            #     print x
            #     print s.text


if __name__ == "__main__":
    keyword, np, pageflush, ipflush, domainflush = readyml()
    for x in keyword:
        flush301(x, np, pageflush)
    fluship(ipflush)
    for x in domainflush:
        flush301(x, np, pageflush)
    fluship(ipflush)
    flushdomain(domainflush)




    # http://202.108.1.122/np/setMemPortalMSG?igId=msw3	msw3为ig号。
    # http://202.108.1.122/np/getKeyword?url=www.hrbonline.com.cn	查询多域名关联的关键词链接。
    # http://www.zhongsou.net/np/php?igId=xihongbin        门户权限串刷新