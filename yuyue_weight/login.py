#*-- coding=utf-8 --*
from selenium import webdriver
import yaml
import time
from robobrowser import RoboBrowser

#dr = webdriver.Firefox()

class Login(object):
    def __init__(self):
        self.dr = webdriver.PhantomJS('phantomjs')
        # self.dr = webdriver.Firefox()
        self.dr.maximize_window()
        self.source = RoboBrowser(history=True)
        print "xxxx"

    def readdata(self, user):
        res = yaml.load(file('ini.yaml'))
        login_url = res['url']['login']
        username = res[user]['username']
        password = res[user]['password']
        xuanchuantu = res['road']['xuanchuantu']
        print username, password
        return login_url, username, password, xuanchuantu

    def login(self, url, username, password):
        # self.dr = webdriver.PhantomJS('phantomjs')
        # # self.dr = webdriver.Firefox()
        # self.dr.maximize_window()
        # self.source = RoboBrowser(history=True)
        self.dr.get(url)
        #动态识别元素id
        self.source.open(url)
        ids = self.source.select('input')
        username_id = str(ids[0].attrs['id'])
        password_id = str(ids[1].attrs['id'])
        button_id = str(ids[2].attrs['id'])
        #页面输入
        self.dr.find_element_by_id(username_id).click()
        self.dr.find_element_by_id(username_id).send_keys(username)
        self.dr.find_element_by_id(password_id).click()
        self.dr.find_element_by_id(password_id).send_keys(password)
        self.dr.save_screenshot('./login.png')
        self.dr.find_element_by_name(button_id).click()
        time.sleep(2)

    #此方法后期可做元素遍历
    def add_jj(self, img):
        print "简介"
        self.dr.find_elements_by_class_name('btn-search')[1].click() #进入新建预约页
        self.dr.find_element_by_id('fileToUpload1').send_keys(img)
        self.dr.find_element_by_class_name('btn-confirm2').click()
        self.dr.find_element_by_name('title').click()
        self.dr.find_element_by_name('title').send_keys('whtest1')
        self.dr.find_element_by_name('leader').click()
        self.dr.find_element_by_name('leader').send_keys('whtest1')
        self.dr.find_element_by_name('tel').click()
        self.dr.find_element_by_name('tel').send_keys('13421111111')
        self.dr.find_element_by_name('location').click()
        self.dr.find_element_by_name('location').send_keys(u'朝阳区')
        self.dr.find_elements_by_tag_name('img')[2].click()
        frame = self.dr.find_elements_by_tag_name('iframe')[0].get_attribute('name')
        self.dr.switch_to_frame(frame)
        self.dr.find_element_by_id('ok').click()
        self.dr.switch_to_default_content()
        select = self.dr.find_elements_by_tag_name('select')
        select[0].find_elements_by_tag_name('option')[1].click()
        time.sleep(2)
        select[1].find_elements_by_tag_name('option')[1].click()
        # self.dr.find_elements_by_tag_name('select')[1].find_elements_by_tag_name('option')[1].click()
        self.dr.save_screenshot('./save.png')
        self.dr.find_element_by_link_text(u'保存').click()

    def add_yyxx(self):
        self.dr.find_element_by_link_text(u'预约信息').click()
        self.dr.find_element_by_name('s_start').send_keys('2015-01-08')
        self.dr.find_element_by_name('s_end').send_keys('2015-01-28')
        self.dr.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div[2]/span[5]/input').click()

    def quit(self):
        time.sleep(5)
        self.dr.quit()


if __name__=='__main__':
    login_url, username, password, xuanchuantu = Login().readdata('player')
    try:
        Login().login(login_url, username, password)
        Login().add_jj(xuanchuantu)
    except Exception,e:
        print e
    Login().quit()
