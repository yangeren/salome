#*-- coding=utf-8--*
__author__ = 'hanz'
from appium import webdriver
import os
import time
# from selenium import webdriver
import unittest

# Returns abs path relative to this file and not cwd
from selenium.webdriver import TouchActions


class Souyue(unittest.TestCase):
    """docstring for Souyue"""
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    desired_caps = {}
    desired_caps['deviceName'] = 'X909'
    desired_caps['browserName'] = ''
    desired_caps['platformVersion'] = '4.2'
    desired_caps['platformName']='Android'
    desired_caps['app'] = PATH('/home/hanz/Downloads/下载手机安装包/souyue_v4.1_20141230.apk')
    # ('/home/hanz/Downloads/下载手机安装包/souyue_v4.1_20141230.apk')
    desired_caps['app-package'] = 'com.zhongsou.souyue'
    desired_caps['app-activity'] = 'com.zhongsou.souyue.activity.SplashActivity'
    print desired_caps
    dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # nowtime = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
    # os.mkdir(str(nowtime))

    #跳过启动图
    def test1(self):
        for i in xrange(4):
            time.sleep(3)
            self.dr.swipe(800, 900, 300, 900, 800)
            print i
        time.sleep(2)

    #选择兴趣圈
    def test2(self):
        imageview = self.dr.find_elements_by_name(u'美食圈')
        self.dr.long_press_keycode()
        for i in imageview:
            i.click()
            time.sleep(0.5)
        # textview = self.dr.find_elements_by_tag_name('TextView')
        # textview[-1].click()

    def test9(self):
        time.sleep(5)
        self.dr.stop_client()
        self.dr.quit()

#def test1(self):
# 跳过启动轮播
# time.sleep(3)
# tg = self.dr.find_elements_by_class_name("android.widget.ImageView")
# print tg
# print len(tg)
# tg[1].click()
# self.dr.execute_script ('mobile: flick', {"startX":"0.9","startX":"0.1"})
# time.sleep(3)
# self.dr.execute_script ('mobile: flick', {"startY":"0.9","startY":"0.1"})
# time.sleep(3)
# self.dr.execute_script("mobile: swipe",{"touchCount": 1, "startX": 157, "startY": 529, "endX": 156, "endY": 102, "duration": 0.5})
# touch_actions = TouchActions(self.dr)
# self.dr.flick_element(pages,0,-500,0).perform()
# touch_actions = TouchActions(dr)
# touch_actions.flick_element('android.widget.ImageView',0,-500,0).perform()
# time.sleep(5)




    # def test3(self):
    #     #遍历图片按钮，并点击左上角
    #     try:
    #         all = self.dr.find_elements_by_xpath("//ImageButton")
    #         print all
    #         all[0].click()
    #     except Exception, e:
    #         print e
    #
    #
    # def test4(self):
    #     pass
    #     #点击进入登陆
    #     lg = self.dr.find_element_by_name(u"账号未登录")
    #     lg.click()
    #
    # def test5(self):
    #     pass
    #     #进入登陆页面，并输入用户名密码
    #     pu = self.dr.find_elements_by_xpath("EditText")
    #     # self.dr.execute_script("mobile: tap", {"touchCount":"1", "x":"0.9","y":"0.8", "element":pu})
    #     # self.dr.execute_script 'mobile:keyevent', {'keycode'=>50,'metastate'=>28672}
    #     pu[0].send_keys("13426152297")
    #
    # def test6(self):
    #     pu = self.dr.find_elements_by_xpath("EditText")
    #     pu[1].send_keys("3212088")
    #     # dl = self.dr.find_elements_by_xpath("//button[@text=u'登陆']")
    #
    # def test7(self):
    #     dl = self.dr.find_elements_by_xpath("//button")
    #     print dl
    #     dl[1].click()
    #     time.sleep(5)
    #     # touch_actions = TouchActions(self.dr)
    #     # touch_actions.flick_element(pages,0,-500,0).perform()
    #
    # def test8(self):
    #     self.dr.back()
    #
    # def test9(self):
    #     sz = self.dr.find_element_by_name(u"设置")
    #     sz.click()
    #
    # def test8(self):
    #     self.dr.quit()
    #
    # def screenshot(self):
    #     time.sleep(1)
    #     nowtime = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
    #     # name = time.time()
    #     self.dr.get_screenshot_as_file("./%s/%s.png" % (str(self.nowtime),str(nowtime)))
    #
    # # def setUp(self):
    # #     print "setUp"
    #
    # # def tearDown(self):
    # #     # time.sleep(5)
    #
    #     # self.screenshot()
    #     # self.dr.quit()
    #
    # # dr.quit()
    #
    # # el = driver.find_element_by_name("Add Contact")
    # # el.click()
    #
    # # textfields = driver.find_elements_by_tag_name("textfield")
    # # textfields[0].send_keys("My Name")
    # # textfields[2].send_keys("someone@somewhere.com")
    #
    # # driver.find_element_by_name("Save").click()

if __name__ == '__main__':
    unittest.main()




'''
下划操作
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions


pages = driver.find_element_by_id("tv.acfundanmaku.video:id/home_channel")
touch_actions = TouchActions(driver)
touch_actions.flick_element(pages,0,-500,0).perform()
'''