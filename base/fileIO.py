#!/usr/bin/python
# -*-coding: UTF-8 -*-

import os

fo = open("foo.txt", "w+")
print "文件名字：", fo.name
print "是否已经关闭1：", fo.closed
print "打开文件的访问模式：", fo.mode
# 文件写入内容 write()方法不会在字符串的结尾添加换行符('\n')：
fo.write("i'm writing something.....\n 第二行文本  \n \n 第四行文本")
# 关闭打开的文件
fo.close()
print "是否已经关闭2：", fo.closed

fo1 = open("foo.txt", "r+")
# read（）方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。  fileObject.read([count])
str = fo1.read(10)
print "str:", str

print "分隔符1：", "--------------------------------"

# 打开一个文件
fo2 = open("foo.txt", "r+")
str = fo2.read(10)
print "读取的字符串是 : ", str

# 查找当前位置
position = fo2.tell()
print "当前文件位置 : ", position

# 把指针再次重新定位到文件开头
position = fo2.seek(0, 0)
str = fo2.read(10)
print "重新读取字符串 : ", str
# 关闭打开的文件
fo2.close()

print "分隔符2：", "--------------------------------"

# 重命名和删除文件
os.rename("foo.txt", "fool2.txt")

# 删除一个已经存在的文件
# os.remove("fool2.txt")

# 创建目录
# os.mkdir("test")

# 改变当前目录
# 将当前目录改为"/home/newdir"
# os.chdir("/home/zhuningning/PycharmProjects/pythonBase/base/test")

# 显示当前目录
print os.getcwd()

# 删除目录
# os.rmdir("/home/zhuningning/PycharmProjects/pythonBase/base/test")

print "分隔符3：", "--------------------------------"

# 每行读取文件
fo = open("fool2.txt", "rw+")
print "文件名为: ", fo.name

for index in range(4):
    line = fo.next()
    print "第 %d 行 - %s" % (index+1, line)

# 关闭文件
fo.close()