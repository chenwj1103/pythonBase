#!/usr/bin/python
# -*- coding: UTF-8 -*-

dDist = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print dDist  # 输出完整列表
print dDist[0]  # 输出列表的第一个元素
print dDist[1:3]  # 输出第二个至第三个元素
print dDist[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print dDist + tinylist  # 打印组合的列表

print 'dDist[0]:', dDist[0]
print 'dDist[2:4]:', dDist[2:4]

dDist.append(5)  # 添加元素
dDist.append('test')

print dDist
del dDist[4]  # 删除元素
print dDist

# 脚本操作
print '列表长度：', len(dDist)  # 长度
print '列表组合：', dDist + tinylist  # 组合
print '列表重复：', dDist * 3
print '某个元素是否在列表中：', 5 in dDist
for x in dDist:
    print '循环元素：', x

lenList = [4, 6, 7, 8, 9]
# 获取列表的长度
print len(lenList)
# 获取列表元素的最大值
print max(lenList)
# 将元祖转化为列表
tup = (5,7,9,0)
print tup
tupList = list(tup)
print tupList

# 添加元素
dDist.append(5)