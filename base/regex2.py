#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

print(re.search('www', 'www.baidu.com').span())
print(re.search('com', 'www.baidu.com').span())

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print "searchObj.group() : ", searchObj.group()
    print "searchObj.group(1) : ", searchObj.group(1)
    print "searchObj.group(2) : ", searchObj.group(2)
else:
    print "Nothing found!!"

phone = '2004-959-559 # 这是一个国外电话号码'

# 删除字符串中的python注释
num = re.sub(r'#.*$', "", phone)
print '电话号码是1：', num

# 删除非数字的字符串
num = re.sub(r'\D', '', phone)
print "电话号码是2：", num

# 测试compile
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print m
m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
print m
m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
print m  # 返回一个 Match 对象
print m.group(0)  # 可省略 0
print m.start(0)  # 可省略 0
print m.end(0)  # 可省略 0
print m.span(0)  # 可省略 0

# 测试findall

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

# 测试re.finditer

it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )