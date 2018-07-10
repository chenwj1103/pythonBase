#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 引入time模块
import time
import calendar
import datetime

# 时间戳
ticks = time.time()
print 'ticks:', ticks

# 获取当前时间,元组形式
localTime = time.localtime(time.time())
print 'localTime:', localTime

# 获取格式化日期
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

# 输出日历
cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal

# 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
print 'timeClock:', time.clock()

# time.sleep(t) Python time sleep() 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。
print "Start : %s" % time.ctime()
time.sleep(10)
print "End : %s" % time.ctime()

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat())
print ("当前的年份是 %s" % i.year)
print ("当前的月份是 %s" % i.month)
print ("当前的日期是  %s" % i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
print ("当前小时是 %s" % i.hour)
print ("当前分钟是 %s" % i.minute)
print ("当前秒是  %s" % i.second)
