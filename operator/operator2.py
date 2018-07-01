#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
c = 0

c = a & b
print 'c===',c

c = a | b
print 'c====',c

c = a ^ b
print 'c====',c

c = - a
print 'c====',c

c = ~a
print "4 - c 的值为：", c # ~x 类似于 -x-1

c = a << 2
print "5 - c 的值为：", c

c = a >> 2
print "6 - c 的值为：", c



