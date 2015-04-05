#*--coding:utf-8--*
__author__ = 'yer'

import requests, time, datetime

# while True:
#     url = 'http://www.zhongguosyzs.com/channel/14023972'
#     res = requests.get(url)
#     print res.content
#     print res.url
#     print res
#     time.sleep(15)

# print datetime.timedelta()
# print datetime.struct_time()

# house = 3000000
# week = 30000
# month = 4
# year = 10
# money = week * month * year
#
# print money
# print house/money
"""
data='''A|100
A|400
A|500
A|800
B|700
B|100
B|300
'''

last_line_one=''
list_tmp=[]
for line in data.strip().split('\n'):
    # print line
    line_list=line.split('|')   #各行的列表
    # print line_list
    line_one=line_list[0]   #得到每行的第一项
    # print line_one
    line_two=line_list[1]   #得到每行的第二项
    list_tmp.insert(0,line_two)        #生成一个临时列表
    # print line_one,last_line_one,'=?'
    if line_one == last_line_one:

        print list_tmp

    else:
        print
        list_tmp=[]
    last_line_one=line_one
"""

"""
def func1(arg1):
    arg1[0] = 12
    return arg1

test = [1,2,3,4]
test1 = (1,2,3,4)
print test
print func1(test)
print test1
print func1(test1)
"""

"""
2 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；

传递3个列表参数：

[1,2,3],[1,5,65],[33,445,22]

返回这3个列表中元素最大的那个，结果是：445
"""

def func1(arg1,arg2,arg3):
    a = []
    if isinstance(arg1,list) and isinstance(arg2, list) and isinstance(arg3, list):
        a = arg1 + arg2 + arg3
        # return max(a) #关键字匹配
        return sorted(a)[-1] #位置匹配
    else:
        return 'error'

print func1([1,2,3],[1,5,65],[33,445,22])

"""
3 递归函数解释，用自己的话说明这个递归函数的工作流程。

def func1(i):
    if i<100:
        return i + func1(i+1)
    return i
print func1(0)
"""
#返回0-99的合
def func1(i):
    if i<100:
        return i + func1(i+1)
    return i
print func1(0)

b =0
for i in xrange(100):
    print i 
    b += i

print b
g = lambda m:[i for i in xrange(10)]
print g(10)

print filter([1,2,3,4,5])