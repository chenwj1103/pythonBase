#!/usr/bin/python
# -*-coding: utf-8 -*-

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
# 问每个月的兔子总数为多少？ 其实是斐波那契数列 1 1 2 3 5 8 13 21


def fib(n):
    f1 = 1
    f2 = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n - 1):
            f1, f2 = f2, f1 + f2
    return f1


print fib(5)
