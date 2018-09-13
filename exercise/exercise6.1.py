#! /usr/bin/python
# -*-coding: utf-8 -*-

# 菲波那切数列 (使用递归)


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print '斐波那契数列实现2：', fib(10)
