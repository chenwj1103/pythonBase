#!/usr/bin/python
# -*-coding: UTF-8 -*-

def printMe(str):
    "打印字符串在标准显示设备上："
    print str
    return


printMe("我要调用用户自定义函数")
printMe("再次调用用户自定义函数")


# 传递不可变对象
def changeInt(a):
    b = a
    a = 10
    print a
    print b
    return


b = 120
changeInt(b)
print b


# 传可变对象实例
def changeMe(myList):
    '''修改传入的列表：'''
    myList.append([1, 4, 6, 8])
    return


myList = [10, 40, 60]
changeMe(myList)
print 'myList', myList


# 不定长参数的

# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print 'var:', var
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

# 匿名函数

sum = lambda num1, num2: num1 + num2

print "相加后的值：", sum(10, 40)
print "相加后的值2：", sum(50, 60)
