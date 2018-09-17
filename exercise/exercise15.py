#!/usr/bin/python
# -*- coding: utf-8-*-


# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。


score = int(raw_input('请输入学生的分数：'))
grade = ''

if score >= 90:
    grade = 'A'
elif 60 <= score <= 89:
    grade = 'B'
elif 0 <= score < 60:
    grade = 'C'
elif score < 0:
    print '输入的数字不是大于0的。'
    exit(0)

print '学员的成绩是：%s' % grade

