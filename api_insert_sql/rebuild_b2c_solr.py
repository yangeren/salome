__author__ = 'Hanz'
import requests

def rebuild(mall_id):
    del_url = 'http://61.135.210.173:8080/search/kp2/update?stream.body=<delete><query>mallId:%s</query></delete>' % mall_id
    comment_url = 'http://61.135.210.173:8080/search/kp2/update?stream.body=<commit/>'
    rebuild_url = 'http://%s.mall.zhongsou.com/kp/page/gsearch/updateIndex?pw=giu2011update&mallId=%s' % (mall_id, mall_id)
    print del_url
    print comment_url
    print rebuild_url
    del_res = requests.get(del_url)
    comment_res = requests.get(comment_url)
    rebuild_res = requests.get(rebuild_url)
    return del_res, comment_res, rebuild_res


dels, comment, rebuild = rebuild('1004105')
print dels.content, comment.content, rebuild.content,



