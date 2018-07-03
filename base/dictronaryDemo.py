#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"

tinydict = {'name': 'john', 'code': '123', 'dept': 'sales'}

print "dict['one']:", dict['one']
print dict[2]
print tinydict
print dict
print tinydict.items()
print tinydict.keys()

# 删除字典字符串
del dict[2]
print "after del:", dict

tinydict = {'name': 'john', 'code': '123', 'dept': 'sales'}
tinySet = {'a', 6, 7}
tinyList = ['f', 7, 9]
tinyTup = (6, 8, 9)
print 'tinydict type:', type(tinydict)
print 'tinySet type:', type(tinySet)
print 'tinyList type:', type(tinyList)
print 'tinyTup type:', type(tinyTup)

print "after del:", dict
dict.clear() # 删除字典的所有元素
print "after clear:", dict

# 直接引用
tinydict1 = tinydict

# 浅copy 深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
tinydict2 = tinydict.copy()
tinydict['name'] = '张三'
del tinydict['name']

print 'tinydict1：', tinydict1
print 'tinydict2：', tinydict2

tinydict2.fromkeys()
tinydict2.get(tinydict['name'], "")
tinydict2.has_key(tinydict['name'])
tinydict2.items()
tinydict2.keys()
tinydict2.setdefault(tinydict['name'], "")
tinydict2.update(tinydict)
tinydict2.values()
tinydict2.pop(tinydict['name'])
tinydict2.popitem()

