#*--coding:utf-8--*
__author__ = 'hanz'
import re

a = 'name=luda; id=123; sex=male; '
pa = re.compile('id=(.+?);')
res = pa.search(a)
if res:
    print res.group(1)
