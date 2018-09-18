#! /usr/bin/python
# -*- coding: utf-8 -*-

# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

m = int(raw_input('请输入数字\n'))
n = int(raw_input('请输入个数\n'))


value = 0
for x in range(n):
    for y in range(x + 1):
        value += m * (10 ** y)


print '求和：%d' % value
