#!/usr/bin/python
# -*- coding: UTF-8-*-

# 字符串第一个字符大写
str = 'hello world '
str = str.capitalize()
print  str

# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串.默认填充字符为空格。
str2 = 'hello world '
str2 = str2.center(20,"*")
print  str2

# 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
str3 = 'hello world '
str3 =str3.count('o',5,len(str3))
print str3

# 以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
str4 = 'hello 中国'
str4 = str4.decode(encoding='UTF-8',errors='strict')

