#!/usr/bin/python
# -*- coding: UTF-8 -*-


try:
    fh = open("testfile.txt", "w")
    fh.write("write someting...")
except IOError:
    print "error: 没有找到文件或者读取文件失败"
else:
    print "内容写入成功！"
    fh.close()

# try finally语句

try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件1，用于测试异常!")
finally:
    print "Error: 没有找到文件或读取文件失败"


# 用户自定义异常

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror, e:
    print e.args

# 使用except而带多种异常类型

try:
    print "正常执行！"
except(IOError, BaseException, IndentationError):
    print "发生异常！"
else:
    print "如果没有异常执行这块代码"
