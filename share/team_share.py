#coding=utf-8
import time,urllib,urllib2,re,datetime
from BeautifulSoup import BeautifulSoup
from datetime import date
import smtplib,unittest
from email.mime.text import MIMEText
from email.header import Header

a = []
def team_share(username,userid,begin_data,end_data):
	url = "http://61.135.210.119:8033/Query.aspx?kw=%s&begin=%s&end=%s" %(userid,begin_data,end_data)
	req = urllib2.Request(url = url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0')
	res = urllib2.urlopen(req)
	html = res.read()
	soup = BeautifulSoup(''.join(html))
	# print re.findall(r'"td_gray\S*\n.*"',html)
	# print soup.findAll("td")
	#取分享数信息
	beautiful_res = soup.findAll("td",{"class" : "td_gray"})
	# print beautiful_res
	a1 = str(beautiful_res)+"</p>"
	# f = open('team_share_%s.html' % date.today(),'a')
	# f.write(username)
	# f.writelines(a1)
	# f.close()
	return a1

def create_html(data):
	data_head = """
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
	     
	    <html xmlns="http://www.w3.org/1999/xhtml">
	    
	<head>
	    <title>超A测试组，微信分享进度</title>
	    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	</head>
		"""

	data_data = data
	data_end = """
	</html>
	"""
	page = data_head+data_data+data_end
	return page

def send_mail(page):
	sender = 'wanghantest@163.com'
	receiver = [
	  'wanghan@zhongsou.com',
	  'pancy@zhongsou.com'
	  ,'longkq@zhongsou.com'
	  ,'liyn@zhongsou.com',
	  'sunmj@zhongsou.com',
	  'yinzhaolong@zhongsou.com',
	  'cuixt@zhongsou.com',
	  'duanli@zhongsou.com',
	  'guran@zhongsou.com',
	  'yahan.liu@iftek.cn',
	  'hehaitong@zhongsou.com',
	  'jinhe@zhongsou.com'
	  ]
	subject = '每周分享数总览'
	smtpserver = 'smtp.163.com'
	username = 'wanghantest@163.com'
	password = 'zhongsou'
	msg = MIMEText(page,'html','utf-8')
	# msg['subject'] = Header(subject, 'utf-8')
	msg['subject'] = subject

	smtp = smtplib.SMTP()
	smtp.connect('smtp.163.com')
	smtp.login(username,password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()


	# for x in xrange(0,6):
	# 	a.append(str(beautiful_res[x].string).strip())
	# print a

starttime = date.today() - datetime.timedelta(datetime.datetime.now().weekday())
endtime = date.today()
# userid = ["yangeren","yanyan_daisy@163.com","18510100281","18810789836","13261386696","13520603415","18611190410","15201272709"]
userid = {
	"王翰":"yangeren",
	"潘春艳":"yanyan_daisy@163.com",
	"尹兆龙":"18500390070",
	"崔学涛":"18810789836",
	"孙铭杰":"13261386696",
	"段莉":"13520603415",
	"李亚娜":"18611190410",
	"龙开权":"15201272709",
	"谷然":"13264096860",
	"刘亚寒":"13621232446",
	"何海彤":"13811008279",
	"金鹤":"18604682867"
	}
comm = ""
if __name__ == '__main__':
	for x in userid:
		print x
		comm =comm + team_share(x,userid[x],starttime,endtime)
		print comm
	# print comm
	page = create_html(comm)
	send_mail(page)



