#!/usr/bin/python
# -*-coding: UTF-8 -*-
import math
from math import floor
import base.rawInput

money = 3000


def AddMoney():
    # 全局变量的使用
    global money
    print 'globals:', globals().keys()
    print 'locals:', locals()
    money = money + 1


print 'money:', money
AddMoney()
print 'money:', money

# dir函数
content = dir(math)
print 'content:', content

print floor(5.8)
