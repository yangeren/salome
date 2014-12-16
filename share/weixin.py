__author__ = 'hanz'
#coding=utf-8
import urllib,urllib2,time,random,string,json,re,requests

#即时取帐号token值作回传
def gettoken():
    	loginurl = 'http://api2.souyue.mobi/d3api2/user/login.groovy?vc=4.0.2&imei=9f46c1c4a8c3dabbd4b95cfeec31a4a6535ed3de&name=yangeren&password=3212088'
        res = requests.get(loginurl)
        resdata = res.json()['body']['token']
        return resdata

#取搜悦新闻的srpid和url链接，分享参数用
def srpid_url(news_url):
	news_decode = urllib.urlencode(sy_news_data)
	news_req = urllib2.Request(url = news_url,data = news_decode)
	# news_req.add_header('Accept-Encoding','gzip')
	news_req.add_header('User-Agent','Android')
	news_json = urllib2.urlopen(news_req)
	news_json_data = news_json.read()
	print news_json_data
# print news_json_data
# js_da = json.dumps(news_json_data)
# print type(js_da)
	srpId = re.findall(r'"\w{32}"',news_json_data)
	url = re.findall(r'"url":\s"http:\S+"',news_json_data)
	return srpId,url
# b = re.match(r'"srpId":\s"\w+"',news_json_data)

# srpId = a.group(0)
# url = b.group(0)
# print srpId,url

#将链接拼起，作分
def wx_share(type,srpId,token,url):
	#platform:3为微信好友分享；platform:4为微信朋友圈分享
	sta_wx_friends = {
		'os':"Android",
		'platform':type,
		"srpid":srpId,
		"model":"X909",
		"useragent":"",
		"token":token,
		"vc":"3.6",
		"url":url,
		"srp":"悦天下"
		}

	wx_share = "http://n.zhongsou.net/souyueapi/sharestats.ashx"
	misson = urllib.urlencode(sta_wx_friends)
	req_wx_friend = urllib2.Request(url = wx_share,data = misson)
	req_wx_friend.add_header('User-Agent','Android')
	res_data1 = urllib2.urlopen(req_wx_friend)
	print  res_data1.read()


sy_news = "http://api2.souyue.mobi/d3api2/webdata/channel.groovy"
sy_news_data = {
	"category":"11221",
	"lastId":"0",
	"token":"",
	"vc":"3.8.2"
}

token = gettoken()
srpId,url = srpid_url(sy_news)
print srpId,url
# login_url = 'http://api2.souyue.mobi/d3api2/user/login.groovy?vc=4.0.1&imei=cac76bf99c861bce038a4792d23732461c43475c&name=yangeren&password=3212088'
# login = requests.get(login_url)
# print login.content

for x in xrange(0,9):
	wx_share(3,srpId[x][1:-1],token,url[x][8:-1])
	print srpId[x][1:-1],url[x][8:-1]
	time.sleep(5)

for x in xrange(0,5):
	wx_share(4,srpId[x][1:-1],token,url[x][8:-1])
	time.sleep(5)


# print b.group(0)
# a = json.dumps(news_json_data)
# b = json.loads(a)
# print repr(news_json_data)
# print type(json.dumps(news_json_data,sort_keys=False))
# print json.dumps(news_json_data,skipkeys=False)

# print news_json_data

# text = "JGood is a handsome boy, he is cool, clever, and so on..."
# m = re.search(r"(\Stitle\S+\s\S+)", news_json_data)
# # m = re.search(r"(\w)", text)
# if m:
# 	print m.group(0), '\n', m.group(1)
# else:
# 	print 'not match'

"""

jifen:
http://api.jifen.zhongsou.com/index.php?s=userscore/get/&vc=3.8.1
appkey=4da74e36-bf77-40e3-df6b-6b0a573773aa&appid=10003&username=13761350563

get_srpId = "http://api2.souyue.mobi/d3api2/webdata/search.result.groovy?keyword=%E4%B8%AD%E6%90%9C&vc=3.3"
req = urllib2.Request(get_srpId)
res = urllib2.urlopen(req)
srpId =  res.read()
# print srpId

# http://api2.souyue.mobi/d3api2/webdata/channel.groovy?category=11221&lastId=0&vc=3.8.2
# http://api2.souyue.mobi/d3api2/webdata/channel.groovy?category=11221&lastId=73982&vc=3.8.2&

http://lhj.zae.zhongsou.com/api/mqlists?uid=123226&sid=040608f1-95eb-4a4a-94d4-a19e54da643a&username=13426152297&appname=%E4%B8%AD%E6%90%9C%E6%90%9C%E6%82%A6&secret_keyt=0564caa131ff8cb3fa800a3fc854b662#
http://lhj.zae.zhongsou.com/api/mqlists?uid=123226&sid=040608f1-95eb-4a4a-94d4-a19e54da643a&username=13426152297&appname=%E4%B8%AD%E6%90%9C%E6%90%9C%E6%82%A6&secret_keyt=0564caa131ff8cb3fa800a3fc854b662#
# weixinfriend
# http://n.zhongsou.net/souyueapi/sharestats.ashx
# os=Android&platform=3&srpid=9c1c1f74e584d62cd4f011cbcbc33141&model=X909&useragent=&token=8d38870c-46c4-4b88-ae47-150c4d9faf01&vc=3.8.2&url=http%3A%2F%2Fz.zhongsou.net%2Fnews%2F080808_74024.html&srp=%E6%82%A6%E5%A4%A9%E4%B8%8B
# os=Android&platform=3&srpid=9c1c1f74e584d62cd4f011cbcbc33141&model=X909&useragent=&token=8d38870c-46c4-4b88-ae47-150c4d9faf01&vc=3.8.2&url=http://z.zhongsou.net/news/080808_74024.html&srp=悦天下
"""

"""
#秒抢中搜币
mq_zsb_url = "http://lhj.zae.zhongsou.com/api/mqlists"

mq_zsb = {
	"uid":"123226",
	"sid":"040608f1-95eb-4a4a-94d4-a19e54da643a",
	"username":"13426152297",
	"appname":"%E4%B8%AD%E6%90%9C%E6%90%9C%E6%82%A6",
	"secret_keyt":"0564caa131ff8cb3fa800a3fc854b662#"
}

"""

"""
#微信及朋友圈分享

def wx_share(type):
	#platform:3为微信好友分享；platform:4为微信朋友圈分享
	sta_wx_friends = {'os':"Android",
		'platform':type,
		"srpid":"9c1c1f74e584d62cd4f011cbcbc33141",
		"model":"X909",
		"useragent":"",
		"token":"8d38870c-46c4-4b88-ae47-150c4d9faf01",
		"vc":"3.8.2",
		"url":"http://z.zhongsou.net/news/080808_74026.html",
		"srp":"悦天下"}

	wx_share = "http://n.zhongsou.net/souyueapi/sharestats.ashx"
	misson = urllib.urlencode(sta_wx_friends)
	req_wx_friend = urllib2.Request(url = wx_share,data = misson)
	res_data1 = urllib2.urlopen(req_wx_friend)
	print  res_data1.read()


for x in xrange(0,21):
	wx_share(3)

for x in xrange(0,14):
	wx_share(4)


"""

"""
friendgrand
http://n.zhongsou.net/souyueapi/sharestats.ashx
os=Android&platform=4&srpid=9c1c1f74e584d62cd4f011cbcbc33141&model=X909&useragent=&token=8d38870c-46c4-4b88-ae47-150c4d9faf01&vc=3.8.2&url=http%3A%2F%2Fz.zhongsou.net%2Fnews%2F080808_74024.html&srp=%E6%82%A6%E5%A4%A9%E4%B8%8B
os=Android&platform=4&srpid=9c1c1f74e584d62cd4f011cbcbc33141&model=X909&useragent=&token=8d38870c-46c4-4b88-ae47-150c4d9faf01&vc=3.8.2&url=http://z.zhongsou.net/news/080808_74024.html&srp=悦天下


sta = {'os':"Android",
	'platform':"4",
	"srpid":"9c1c1f74e584d62cd4f011cbcbc33141",
	"model":"X909",
	"useragent":"",
	"token":"8d38870c-46c4-4b88-ae47-150c4d9faf01",
	"vc":"3.8.2",
	"url":"http://z.zhongsou.net/news/080808_74024.html",
	"srp":"悦天下"}



http://61.135.210.178/etaoXML/download.action
mallInfoBean.mallId=75
mallInfoBean.mallDomain=www.yatalanmall.com
mallInfoBean.imgDomain=image.yatalanmall.com
mallInfoBean.brand=雅特蓝家纺
mallInfoBean.mallName=雅特蓝家纺商城
mallInfoBean.mallService=正品保证 //七天退货//金牌服务
mallInfoBean.mallCity=浙江省宁波市
mallInfoBean.mallDesc=雅特蓝家纺商城，是由宁波格尔佳网络科技有限公司与北京中搜网络技术有限公司强强联手打造，最新最全面的家用纺织品展示，专业及时的行业新闻与资讯，“引领时尚家居生活潮流”的综合性家用纺织用品网络购物平台。
dataType=2
"""


"""
#门户后台推送
url = "http://www.zhongsou.net/space/admin.php"

data = {
	"op":"SyhPushInfoAjax",
	"igId":"%E5%B0%8F%E5%85%94%E5%AD%90%E4%B9%96%E4%B9%96",
	"title":"标题：此条请拒绝，谢谢",
	"intro":"标题：此条请拒绝，谢谢",
	"xeditor":"标题：此条请拒绝，谢谢",
	"province":"河北省",
	"city":"",
	"os":"",
	"push_count":"",
}

js = urllib.urlencode(data)
req = urllib2.Request(url = url,data = js)
res = urllib2.urlopen(req)
print res.read()

中搜币商城
http://n.zhongsou.net/d3wap/mall/index.aspx?userid=25025&anonymous=1&wifi=1&imei=f81eb3a2aa6cea8f2070e4042db7a0be712ea181&username=yangeren&sid=8d38870c-46c4-4b88-ae47-150c4d9faf01&appname=%E4%B8%AD%E6%90%9C%E6%90%9C%E6%82%A6&v=3.9&type=ios&lat=39.982239&long=116.409698&_s=c5bd6d23cccfc9b4da39749eba86785f


http://n.zhongsou.net/d3wap/mall/index.aspx?userid=129481&anonymous=1&wifi=1&imei=f81eb3a2aa6cea8f2070e4042db7a0be712ea181&username=4GMb9DYkdL@qq.com&sid=669e08dd-2509-443b-a942-5a929279782c&appname=%E4%B8%AD%E6%90%9C%E6%90%9C%E6%82%A6&v=3.9&type=ios&lat=39.982239&long=116.409698&_s=c5bd6d23cccfc9b4da39749eba86785f



"""
