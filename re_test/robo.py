__author__ = 'hanz'
#*--coding=utf-8--*
import re
from robobrowser import RoboBrowser
from BeautifulSoup import BeautifulSoup

dr = RoboBrowser(history=True)
dr.open('http://yuyueweijian.test.zae.zhongsou.com/user/login')

titles = dr.select('input')
for title in titles:
    print title.attrs['id'],title.attrs['name']
