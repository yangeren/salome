from selenium import webdriver
import time

dr = webdriver.Firefox()
newun_url = 'http://newun.zhongsou.com/pkeyword/changeuser/changeLoginUser.jsp?flag=1'
ig_id = 'meijianhua'
zhanhui_url = 'http://www.zhongsou.net/space/admin.php?op=ExhibitList&caid=0&coid=0&sw=&t=0&igId=%E5%95%86%E4%B8%9A%E5%B1%95%E7%A4%BA&page=1'
dr.get(newun_url)
a = dr.switch_to_alert()
a.accept()
dr.find_element_by_id('igNo').send_keys(ig_id)
dr.find_element_by_id('del').click()
a = dr.switch_to_alert()
a.accept()
time.sleep(5)
dr.get(zhanhui_url)
time.sleep(5)
dr.find_element_by_id('chooseAll').click()
time.sleep(5)

for x in range(20):
    dr.find_element_by_link_text('批量删除').click()
    b = dr.switch_to_alert()
    b.accept()
    time.sleep(5)
dr.close()
