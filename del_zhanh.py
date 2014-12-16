#*--coding=utf-8--*
from selenium import webdriver
import time
dr = webdriver.Firefox()

def chuansuo(ig_id):
    newun_url = 'http://newun.zhongsou.com/pkeyword/changeuser/changeLoginUser.jsp?flag=1'
    dr.get(newun_url)
    a = dr.switch_to_alert()
    a.accept()
    dr.find_element_by_id('igNo').send_keys(ig_id)
    dr.find_element_by_id('del').click()
    b = dr.switch_to_alert()
    b.accept()

def delzh(keyword):
    zhanhui_url = 'http://www.zhongsou.net/space/admin.php?op=ExhibitList&caid=0&coid=0&sw=&t=0&igId=%s&page=1' %keyword
    time.sleep(5)
    dr.get(zhanhui_url)
    time.sleep(5)
    dr.find_element_by_id('chooseAll').click()
    time.sleep(5)
    for x in range(70):
        try:
            dr.find_element_by_link_text('批量删除').click()
            b = dr.switch_to_alert()
            b.accept()
            time.sleep(5)
        except Exception, e:
            print(x,e)
    dr.close()


if __name__=="__main__":
    chuansuo("meijianhua")
    delzh('商业展示')