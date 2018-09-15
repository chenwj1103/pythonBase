#! /usr/bin/python
# -*- coding: utf-8 -*-


# 暂停一秒输出


import time

list = [3, 5, 6, 7, 1, 3, 2]

for x in list:
    print x
    time.sleep(1)

dic = {"key": 1, "value": 4}

for y in dic.viewvalues():
    print y
    time.sleep(2)
