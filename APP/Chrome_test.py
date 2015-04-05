__author__ = 'Hanz'
#condig=utf-8
from selenium import webdriver
mobile_emulation = { "deviceName": "Google Nexus 5" }
chrome_options = webdriver.ChromeOptions() #  ChromeOptions实例,也算非常常用的一个类了。
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                          desired_capabilities = chrome_options.to_capabilities())