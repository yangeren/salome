#coding=utf-8
__author__ = 'Hanz'
from selenium import webdriver
dr = webdriver.PhantomJS('phantomjs')
dr.get('http://www.sina.com')
print dr.current_url
dr.quit()