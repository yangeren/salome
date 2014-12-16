__author__ = 'hanz'
#*--coding=utf-8--*
import requests
import os
import re
import yaml
import time

#读配置文件setting.yaml
def readyml():
    readdata = yaml.load(file('setting.yaml'))
    quanzi = readdata['quanzi']
    id = readdata['srpid'].split(' ')
    member = readdata['member']
    print quanzi, id, member
    return quanzi, id, member


#登陆帐号获取最新token
def gettoken(username,password):
    loginurl = 'http://api2.souyue.mobi/d3api2/user/login.groovy'
    data = {
        'vc': '4.0.2',
        'imei': '9f46c1c4a8c3dabbd4b95cfeec31a4asdfasdf',
        'name': username,
        'password': password
    }
    try:
        login_res = requests.get(loginurl, params=data)
        token = login_res.json()['body']['token']
    except Exception, e:
        print '获取token失败'
        print login_res.json(),e
    return token

#加入圈子
def addin(token, interest_id):
    url = 'http://api2.souyue.mobi/d3api2/interest/interest.subscriber.groovy'
    data = {
        'vc': '4.0.2',
        'state': 5,
        'token': token,
        'interest_ids': interest_id
    }
    ms = requests.get(url, params=data)
    print ms.content

#获取圈子资讯列表id
def geturl(quanzi, id, token):
    url = 'http://api2.souyue.mobi/d3api2/webdata/homepage.news.groovy'
    data = {
        "vc": "4.0.2",
        "type": "interest",
        "keyword": quanzi,
        "srpId": id,
        "lastId": "0",
        "token": token
    }
    a = requests.get(url, params=data)
    b = a.json()['body']
    news_id = []
    interest_id = []
    for x in b:
        print x['id'],x['interest_id']
        news_id.append(x['id'])
        interest_id.append(x['interest_id'])
    return news_id

#提交评论
def comment(content, token, id, interest_id):
    pl_url = 'http://api2.souyue.mobi/d3api2/interest/blog.save.groovy?vc=4.0.2'
    data = {
        "blog_id": "0",
        "content": content,
        'image': [],
        "mblog_id": id,
        "token": token,
        "user_ids": "",
        "interest_id": interest_id,
        "title": ""
    }
    print data
    pl = requests.post(pl_url, data=data)
    print pl.content

if __name__=="__main__":
    quanzi, id, member = readyml()
    print member
    #遍历配置文件中的圈子
    for m in quanzi:
        print m
        print quanzi[m]
        #遍历配置文件中的用户
        for x in member:
            token = gettoken(x, member[x])
            addin(token, quanzi[m])
            news_id = geturl(m,quanzi[m],token)
            #遍历圈子中的资讯
            for y in news_id:
                print token, y, quanzi[m]
                comment(u'顶顶顶顶顶顶顶', token, y, quanzi[m])
                time.sleep(5)
    # token = gettoken()
    # geturl()
    # comment(u'真心是好东西', '5e76493c-a698-48a6-8382-6e994fd47d3e', '1108130', '299')


# 加入该圈：
# http://api2.souyue.mobi/d3api2/interest/interest.subscriber.groovy?vc=4.0.2&state=5&token=4b9be219-462e-4ce4-862e-70ff4fa52ae4&interest_ids=300

# 指定兴趣圈
# http://api2.souyue.mobi/d3api2/webdata/homepage.news.groovy?vc=4.0.2&type=interest&keyword=%E6%90%8F%E5%87%BB%E5%9C%88&srpId=68&lastId=0&token=d2a4ab51-240b-42db-a0de-181cc413bdac

# 评论
# http://api2.souyue.mobi/d3api2/interest/blog.save.groovy?vc=4.0.2
# 参数：
# blog_id=&
# content=%E4%B8%8D%E9%94%99&
# mblog_id=1102077&
# token=d2a4ab51-240b-42db-a0de-181cc413bdac&
# user_ids=&
# interest_id=68&
# title=

# android评论：
# http://api2.souyue.mobi/d3api2/interest/blog.save.groovy?vc=4.0.2
# content=%E5%AE%89%E5%A5%BD&mblog_id=1098236&title=&token=0f999fc0-9e6a-482d-af33-227fcbda0db5&interest_id=300&blog_id=0&state=5&images=%5B%5D&vc=4.0.2&user_ids=
# 返回：
# {
#     "head": {
#         "status": 200,
#         "hasMore": false
#     },
#     "body": {
#         "state": 1,
#         "blog_id": 1105746,
#         "srp_id": "21cd1526e7a1f9057e41f1b95fcc615c",
#         "srp_word": "搏击圈"
#     }
# }


# 'www.clgt.com','www.chinaqlw.com','www.hljshangdao.cn','www.zypco.com','www.rafscl.com','www.rujiajituan.com','www.hrbypx.com','www.hrbjxwsp.cn','www.jinghua-group.com','www.cyjtss.cn','www.jinqiaocaiyin.cn','www.sdny88.com','www.cqwufeng.com','www.beijingruntang.com','www.hengdaxs.com','www.zgkywzltw.com','www.maowenjun.com','www.hrbrhqd.cn','www.hljqgxh.com','www.hljyuxing.com','www.fyrngc.com','www.hrbmrsp.cn','www.hrbdinglong.cn','www.rgjkkj.com','www.hangecehua.com','www.yifanlaowu.cn','www.xuansesheying.com.cn','www.tyymqhg.cn','www.bbw678.com','www.gaoshuang1029.com','www.libai.com','www.gexinghuahy.com','www.xixi_luo.com','www.zxyys.com','www.gaoshuang1029.com','www.hlservice.com.cn','www.zgptw.com.cn','www.958ly.com','www.ny168.org','www.bjcre.com','www.gaoshuangmall.com','www.lidabai.com','www.bjyifuyuan.com','www.cptest.com','www.ruiqiu.net','jd.cfsbcn.com','www.cnljjgs.com','www.mcy948.com','www.hljmrnj.com','www.duoshengda.com','www.runheyjs.com','www.gexinghuazz.com','www.xinxin.com','www.13313644999.com','www.xm-hs.net','www.yiyanghudie.com','www.nmlj.cn','www.hljjunchen.com','www.xiyuanshiye.com','www.hrbzlsc.com','www.weidabl.com','www.weilailu.com.cn','www.bbglt.com','www.hrbydxh.com','www.weixinshichang.cn','www.afw365.com','www.zgtsfood.com','www.zgthmhw.com','www.clgt.mobi','www.xinxinxiangyin.com','www.xsfbkg.mobi','www.xiyuansuye.com','catickitchen.com','expohlj.com','dlhzw.cn','xshlmj.com','huadongheb.com','chinalhtx.com'



