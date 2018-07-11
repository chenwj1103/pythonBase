#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:
    parentAttr = 100

    def __init__(self):
        print "调用父类的构造函数"

    def parentMethod(self):
        print "调用父类的方法"

    def setattr(self, value):
        Parent.parentAttr = value

    def getAttr(self):
        print "父类属性：", Parent.parentAttr


class Child(Parent):

    def __init__(self):
        print "调用子类构造方法"

    def childmethod(self):
        print "调用子类的方法"


c = Child()
c.childmethod()
c.parentMethod()
c.setattr(200)
c.getAttr()
