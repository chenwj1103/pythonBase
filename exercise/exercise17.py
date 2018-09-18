#! /usr/bin/python
# -*- coding: utf-8 -*-

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import string

str = raw_input('请输入一个字符串：\n')

letters = 0
space = 0
digit = 0
others = 0

for x in str:
    if x.isalpha():
        letters += 1
    elif x.isspace():
        space += 1
    elif x.isdigit():
        digit += 1
    else:
        others = +1

print 'chars=%d,space=%d,digit=%d,others=%d' % (letters, space, digit, others)
