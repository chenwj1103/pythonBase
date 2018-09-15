#!/usr/bin/python
# -*- coding: utf-8 -*-

# 暂停一秒输出，并格式化当前时间。
import time

listValue = [3, 4, 5, 6, 7, 8]
for x in range(len(listValue)):
    print listValue[x]
    time.sleep(1)
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
