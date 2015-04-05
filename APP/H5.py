import time

__author__ = 'hanz'
#*-- coding=utf-8 --*
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
mobile_emulation = {
    "deviceMetrics": {
        "width": 360, "height": 640, "pixelRatio": 3.0
    },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4"
}

chrome_options = Options()
chrome_path = "C:\Users\H\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

# 解决打开浏览器报警告
chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options = chrome_options, executable_path=chrome_path)
# driver = webdriver.Chrome(executable_path=chrome_path)
# driver.get("http://www.taobao.com")
time.sleep(5)
driver.quit()

# chrome_path = "C:\Users\H\AppData\Local\Google\Chrome\Application\chromedriver_x64.exe"
# dr = webdriver.Chrome(chrome_path)
