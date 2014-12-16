__author__ = 'hanz'
#*--coding=utf8--*

import urllib2
import re

"""
Login to Sina Weibo with cookie
"""

COOKIE = 'UOR=www.lupaworld.com,widget.weibo.com,login.sina.com.cn; SINAGLOBAL=3794161271295.7905.1415926567930; ULV=1418174785470:5:3:2:9252720642096.375.1418174785374:1418102895810; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhQNEDIrM.UJOrDkTx21-yL5JpX5KMt; un=xiaoyaoyangeren@163.com; TC-Ugrow-G0=1ae767ccb34a580ffdaaa3a58eb208b8; SUS=SID-1659508761-1418174801-XD-2qc4k-f93e3c0f4c2667036f8cda7f67fea041; SUE=es%3D823cc661b885f9986cfdf2131bd074ef%26ev%3Dv1%26es2%3De2150de5bd00b984dc02fa2f6089cc95%26rs0%3DStuA9tunJhG9DUUy1mgIaK3u%252B81Zb%252BTDPrFFuNFJAF2tMZ3NZiCQwFWkLFXxiMnH2q6yOeJaKnWGoJX6F3RbXIUfQkQhbfW8SxITGWZWH9A25PC2Eswcb0RnG0%252FPXy64IjWLBiOAoYk8XNEySurdvQMH4Oa5PXUzW5vFOrCC1Rw%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1418174801%26et%3D1418261201%26d%3Dc909%26i%3Da041%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D0%26st%3D0%26uid%3D1659508761%26name%3Dxiaoyaoyangeren%2540163.com%26nick%3D%25E5%2585%25BB%25E9%25B9%2585%25E4%25BA%25BA%26fmp%3D%26lcp%3D2014-12-09%252013%253A31%253A04; SUB=_2A255g9EBDeTxGedI7lsU8CbLzT2IHXVa-_NJrDV8PUNbvtAPLUPGkW9p9hg4VcLZvTG7wydX2QEa2P8GAg..; ALF=1449710799; SSOLoginState=1418174801; wvr=6; TC-V5-G0=31f4e525ed52a18c5b2224b4d56c70a1; _s_tentry=login.sina.com.cn; Apache=9252720642096.375.1418174785374' #fill with your weibo.com cookie
HEADERS = {"cookie": COOKIE}

def test_login():
    url = 'http://weibo.com'
    req = urllib2.Request(url, headers=HEADERS)
    text = urllib2.urlopen(req).read()

    pat_title = re.compile('<title>(.+?)</title>')
    r = pat_title.search(text)
    if r:
        print r.group(1)


if __name__ == '__main__':
    test_login()