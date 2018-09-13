#!/usr/bin/python
# -*- coding: utf-8-*-

# 斐波那契数列


def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


# 输出第10个斐波那契数列
print '斐波那契数列实现1', fib(10)



