#! /usr/bin/python
# -*- coding: utf-8 -*-

# 判断101-200之间有多少个素数，并输出所有素数。
# 思路 首先确定最外层循环，其次是求出循环的数的平方根（原因：假如一个数是 25 求出平方根5。 25 除  2 3 4 5 6 就可以，不需要除大于6的了）

from math import sqrt

count = 0
pn = 1

for i in range(101, 201):
    k = int(sqrt(i))
    for j in range(2, k + 1):
        if i % j == 0:
            pn = 0
            break
    if pn == 1:
        count += 1
        print i
    pn = 1

print 'total number is %d' % count
