__author__ = 'hanz'
#*-- coding=utf-8 --*
import login
import time
from selenium import webdriver

class Add_yyxx():
    # def __init__(self):
    #     self.dr = webdriver.PhantomJS('phantomjs')

    def add_yyxx(self,img):
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


if __name__=='__main__':
    Add_yyxx().add_yyxx()

