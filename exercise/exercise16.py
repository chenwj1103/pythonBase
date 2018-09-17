#! /usr/bin/python
# -*- coding: utf-8-*-

# 输出指定格式的日期。

import datetime

# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print '当前时间', datetime.date.today().strftime('%d/%m/%Y')
# 创建日期对象
makeBirthDate = datetime.date(1990, 11, 03)

print makeBirthDate.strftime('%d/%m/%Y')
# 日期算术运算
miyazakiBirthNextDay = makeBirthDate + datetime.timedelta(days=1)

print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

makeBirthDate = makeBirthDate.replace(year=makeBirthDate.year + 1)

print makeBirthDate.strftime('%d/%m/%Y')
