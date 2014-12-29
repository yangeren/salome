#*-- coding=utf-8 --*
from selenium import webdriver
import yaml
import time

dr = webdriver.Firefox()
dr.maximize_window()

def readdata(user):
    res = yaml.load(file('ini.yaml'))
    login_url = res['url']['login']
    username = res[user]['username']
    password = res[user]['password']
    xuanchuantu = res['road']['xuanchuantu']
    print username,password
    return login_url, username, password, xuanchuantu

def login(url, username, password):
    dr.get(url)
    dr.find_element_by_id('username').click()
    dr.find_element_by_id('username').send_keys(username)
    dr.find_element_by_id('password').click()
    dr.find_element_by_id('password').send_keys(password)
    dr.find_element_by_name('button').click()
    time.sleep(2)

#此方法后期可做元素遍历
def add_jj(img):
    dr.find_elements_by_class_name('btn-search')[1].click() #进入新建预约页
    dr.find_element_by_id('fileToUpload1').send_keys(img)
    dr.find_element_by_class_name('btn-confirm2').click()
    dr.find_element_by_name('title').click()
    dr.find_element_by_name('title').send_keys('whtest1')
    dr.find_element_by_name('leader').click()
    dr.find_element_by_name('leader').send_keys('whtest1')
    dr.find_element_by_name('tel').click()
    dr.find_element_by_name('tel').send_keys('13421111111')
    dr.find_element_by_name('location').click()
    dr.find_element_by_name('location').send_keys(u'朝阳区')
    dr.find_elements_by_tag_name('img')[2].click()
    frame = dr.find_elements_by_tag_name('iframe')[0].get_attribute('name')
    dr.switch_to_frame(frame)
    dr.find_element_by_id('ok').click()
    dr.switch_to_default_content()
    select = dr.find_elements_by_tag_name('select')
    select[0].find_elements_by_tag_name('option')[1].click()
    time.sleep(2)
    select[1].find_elements_by_tag_name('option')[1].click()
    # dr.find_elements_by_tag_name('select')[1].find_elements_by_tag_name('option')[1].click()
    dr.find_element_by_link_text(u'保存').click()




def quit():
    time.sleep(5)
    dr.quit()

if __name__=='__main__':
    login_url, username, password, xuanchuantu = readdata('player')
    try:
        login(login_url, username, password)
        add_jj(xuanchuantu)
    except Exception,e:
        print e
    quit()