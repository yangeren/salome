__author__ = 'hanz'
# *--coding=utf-8--*
import requests
import re


# def test_cookie(url, testcookie):
#     HEADERS = {"cookie": testcookie}
#     res = requests.get(url, cookies=testcookie)
#     print res.text

# url = 'http://httpbin.org/cookies'
url = 'http://vsht.zhongsou.net/autopack/syhbq/list'
# cookies = dict(cookies_are='working', list='list')
# cookies = {}
cookies = dict(loginname='chenyh@zhongsou.com',stat_cid='1216111411130910',__utma='12958760.487158782.1415848573.1418095302.1418200584.37',__utmz='12958760.1418015958.34.4.utmcsr=uid.zhongsou.com|utmccn=(referral)|utmcmd=referral|utmcct=/zspassport/logout.aspx',Hm_lvt_7d88ad9993d03e77d065a8948f372bbd='1417765019,1418015958,1418095302,1418200584',dall='_cur%3D13899865%7C',lzstat_uv='3347141796940753258|1355895@2725122@1096102',un_web='vs_chenyh',nn_web='',u_city='%e5%8c%97%e4%ba%ac%e5%b8%82%3a%e8%a5%bf%e5%9f%8e%e5%8c%ba',uniid='tykgbq8z2slukkhmh4hgzn87',sessid='a0vj4diulki7in1320pz7hrdpa9kdwvp0lje5erc',ver='2.5',token='',u_county='YXNkZkA5OTl%2bf2l6X0usBVmS%2fYO4zRor8xTbF3bwwiSIo0bUfP3722fJzAUCwa0Odk6qqQ7AwylBU3oqMDk%3d',access_token='%2b8CvrmzyDTky%2be6gVwfryOqAzKyABzTORHTDNhcoVBRd%2f0PJ0MeeXBPL2hg8uUtnvSP7J4MauYxzAKdTfJoMXw%3d%3d',access_uid='500001',Hm_lpvt_7d88ad9993d03e77d065a8948f372bbd='1418200584',__utmc='12958760')
r = requests.get(url, cookies=cookies)
print r.content


# url = 'http://vsht.zhongsou.net/autopack/syhbq/list'
# testcookie = {loginname=chenyh@zhongsou.com; stat_cid=1216111411130910; __utma=12958760.487158782.1415848573.1418095302.1418200584.37; __utmz=12958760.1418015958.34.4.utmcsr=uid.zhongsou.com|utmccn=(referral)|utmcmd=referral|utmcct=/zspassport/logout.aspx; Hm_lvt_7d88ad9993d03e77d065a8948f372bbd=1417765019,1418015958,1418095302,1418200584; dall=_cur%3D13899865%7C; lzstat_uv=3347141796940753258|1355895@2725122@1096102; un_web=vs_chenyh; nn_web=; u_city=%e5%8c%97%e4%ba%ac%e5%b8%82%3a%e8%a5%bf%e5%9f%8e%e5%8c%ba; uniid=tykgbq8z2slukkhmh4hgzn87; sessid=a0vj4diulki7in1320pz7hrdpa9kdwvp0lje5erc; ver=2.5; token=; u_county=YXNkZkA5OTl%2bf2l6X0usBVmS%2fYO4zRor8xTbF3bwwiSIo0bUfP3722fJzAUCwa0Odk6qqQ7AwylBU3oqMDk%3d; access_token=%2b8CvrmzyDTky%2be6gVwfryOqAzKyABzTORHTDNhcoVBRd%2f0PJ0MeeXBPL2hg8uUtnvSP7J4MauYxzAKdTfJoMXw%3d%3d; access_uid=500001; Hm_lpvt_7d88ad9993d03e77d065a8948f372bbd=1418200584; __utmc=12958760}


# testcookie = dict{
#     loginname:'chenyh@zhongsou.com';
#     stat_cid:'1216111411130910';
#     __utma='12958760.487158782.1415848573.1418095302.1418200584.37';
#     __utmz='12958760.1418015958.34.4.utmcsr=uid.zhongsou.com|utmccn=(referral)|utmcmd=referral|utmcct=/zspassport/logout.aspx';
#     Hm_lvt_7d88ad9993d03e77d065a8948f372bbd='1417765019,1418015958,1418095302,1418200584';
#     dall='_cur%3D13899865%7C';
#     lzstat_uv='3347141796940753258|1355895@2725122@1096102';
#     un_web='vs_chenyh';
#     nn_web='';
#     u_city='%e5%8c%97%e4%ba%ac%e5%b8%82%3a%e8%a5%bf%e5%9f%8e%e5%8c%ba';
#     uniid='tykgbq8z2slukkhmh4hgzn87';
#     sessid='a0vj4diulki7in1320pz7hrdpa9kdwvp0lje5erc';
#     ver='2.5';
#     token='';
#     u_county='YXNkZkA5OTl%2bf2l6X0usBVmS%2fYO4zRor8xTbF3bwwiSIo0bUfP3722fJzAUCwa0Odk6qqQ7AwylBU3oqMDk%3d';
#     access_token='%2b8CvrmzyDTky%2be6gVwfryOqAzKyABzTORHTDNhcoVBRd%2f0PJ0MeeXBPL2hg8uUtnvSP7J4MauYxzAKdTfJoMXw%3d%3d';
#     access_uid='500001';
#     Hm_lpvt_7d88ad9993d03e77d065a8948f372bbd='1418200584';
#     __utmc='12958760'
#     }


# if __name__ == '__main__':
#     test_cookie(url, testcookie)