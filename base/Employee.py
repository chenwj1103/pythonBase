#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    ' 所有员工的基类 '
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "total employee %d" % Employee.empCount

    def displayEmployee(self):
        print "name:", self.name, ",salary:", self.salary


# empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
# 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
# self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。


emp1 = Employee("lee", 2000)
emp2 = Employee("zhang", 4000)

emp1.displayCount()
emp2.displayEmployee()

print "total employee %d" % Employee.empCount



emp1.age = 10
print "emp1 age: %d" % emp1.age
emp1.age = 20 # 修改属性值
print "after emp1 age: %d" % emp1.age
# del emp1.age


print hasattr(emp1, 'age')
print getattr(emp1, 'age')
print setattr(emp1, 'age', 30)
print getattr(emp1, 'age')
print delattr(emp1, 'age')

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
