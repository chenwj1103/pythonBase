#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Test:
    def prt(self):
        print(self)  # <__main__.Test instance at 0x7ff0abb9f290>
        print(self.__class__)  # __main__.Test


t = Test()
t.prt()
