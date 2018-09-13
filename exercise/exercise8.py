#! /usr/bin/python
# -*- coding: utf-8 -*-

# 打印乘法口诀


for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print "%d*%d=%d" % (i, j, i*j),
        else:
            print
            break

