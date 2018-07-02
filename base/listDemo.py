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
tup = (5, 7, 9, 0)
print tup
tupList = list(tup)
print tupList
# 添加元素
tupList.append(5)
# 统计某个元素在列表中出现的次数
n = tupList.count(5)
print '元素在列表中出现的次数：', n

# 一次性扩展多个值
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)

# 列出某个元素在列表中的位置
bList.index(123)

# 在某个位置插入某个元素
list.insert(3, 'dddd')

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
bList.pop(-1)

# 移除列表中某个值的第一个匹配项
bList.remove(5)

'''
cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
'''
# 排序
list.sort(cmp=None, key=None, reverse=False)