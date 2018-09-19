#!/usr/bin/python
# -*- coding:utf-8-*-
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

tour = 100.0
height = 100.0

for n in range(0, 10):
    tour = tour + height
    height /= 2

print '经过的距离为：', tour
print '最后的高度为:', height
