#!/usr/bin/python
# -*-coding:utf-8 -*-

# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

a = int(raw_input('请输入a：'))
b = int(raw_input('请输入b：'))
c = int(raw_input('请输入c：'))

l = []
l.append(a)
l.append(b)
l.append(c)

n = len(l)
for x in range(0, n - 1):
    for y in range(1, n):
        if l[x] > l[y]:
            temp = l[x]
            l[x] = l[y]
            l[y] = temp

print l
