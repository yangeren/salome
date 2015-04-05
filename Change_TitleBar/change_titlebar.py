# coding=utf-8
__author__ = 'Hanz'
import requests
import time

def titlebar(md5, system):
    url = 'http://edit.zhongsou.com/Webapi/GetWidgetInfo'
    res_data = {
    	'srpid': md5,
    	'sign': '41f2b372eb596b7337ed0ce229c2ba45',
    	'title': system,
    	'pagesize': 30
    }
    # print res_data
    q = requests.post(url, data=res_data)
    result = q.json()
    print result
    mr_android = [
        'trade_ac_all_title_bg_red.png',
        'trade_ac_btn_goback_selector.9.png',
        'trade_ac_btn_goback_selector_h.9.png',
        'trade_ac_imgbtn_menu_normal.9.png',
        'trade_ac_imgbtn_menu_selected.9.png',
        'trade_ac_srp_subcribe_normal.9.png',
        'trade_ac_srp_subcribe.9.png',
        'trade_ac_title_super_image.png',
        'trade_ac_im_chat_pop_bgp',
        'trade_ac_im_chat_pop_bg',
        'trade_ac_word_color',
        'trade_ac_pop_zuti.png',
        'trade_ac_pop_erweima.png',
        'trade_ac_pop_fenxiang.png',
        'trade_ac_pop_tuiding.png',
        'trade_ac_srp_no_sub_normal.9.png',
        'trade_ac_srp_no_sub_selected.9.png',
        'trade_ac_srp_create_shortcut.png',
        'trade_ac_btn_refresh_enable.9.png',
        'trade_ac_btn_refresh_unenabled.9.png',
        'trade_ac_btn_refresh_selected.9.png',
        # 'sdf'
    ]
    #判断资源个数是否正确
    titles = []
    for m in result['list']:
        titles.append(m['title'])

    if len(mr_android) == len(titles):
        print u'资源数目正确，共%s个。' % len(mr_android)
    else:
        print u'标准资源数目为：%s，实际上传资源数目为：%s。' % (len(mr_android), len(result['list']))

    #判断资源名是否正确
    for x in mr_android:
        if x in titles:
            pass
        else:
            print "缺少资源图：%s" % x
            # print titles

    # print result['list']
    # print len(result['list'])


titlebar('183b720f4ada150ada8a54cf0a836837',u'title_android')

# "keyword": "托尼托尼·乔巴",
# "srpId": "183b720f4ada150ada8a54cf0a836837",
# "keyword": "华野户外3",
# "srpId": "7fd1f75714c31bc098ba1643d747ba71",
# title_android
# title_ios