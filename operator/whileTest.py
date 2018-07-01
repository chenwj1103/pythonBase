#!/usr/bin/python
# -*- coding: UTF-8 -*-

i = 1
while i < 10:
    i += 1
    print i
else:
    print "end！"

print "----------"

i = 2
while i < 20:
    i += 1
    if i % 2 == 0:
        break # continue
    print "i==",i
else:
    print 'end'

