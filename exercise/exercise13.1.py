#! /usr/bin/python
# -*- coding: utf-8 -*-

# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for x in range(1, 10):
    for y in range(0, 10):
        for z in range(0, 10):
            s1 = x * 100 + y * 10 + z
            s2 = x ** 3 + y ** 3 + z ** 3
            if s1 == s2:
                print '水仙花数有：%3ld' % s1
