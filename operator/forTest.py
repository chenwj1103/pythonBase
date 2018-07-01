#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 遍历字符串
for letter in "python":
    print '当前字母：',letter


# 遍历list
fruits = ['apple', 'banana', 'peer']
for fruit in fruits:
    print '当前水果为：', fruit

# 通过下标遍历list
for index in range(len(fruits)):
    print '通过下标获取的水果的名字为：', fruits[index]