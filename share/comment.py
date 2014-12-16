__author__ = 'hanz'
#*--coding=utf-8--*
import requests
import os
import re

def geturl():
    pass
    url = 'http://api2.souyue.mobi/d3api2/webdata/homepage.news.groovy?vc=4.0.2&type=interest&keyword=%E6%90%8F%E5%87%BB%E5%9C%88&srpId=68&lastId=0&token=d2a4ab51-240b-42db-a0de-181cc413bdac '
    a = requests.get(url)
    a.content