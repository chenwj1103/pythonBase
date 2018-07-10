#!/usr/bin/python
# -*-coding= UTF-8 -*-

import MySQLdb

# 反转函数 revert1
def revert(myList):
    for i in range(0, len(myList) / 2):
        temp = myList[i]
        myList[i] = myList[-i - 1]
        myList[-i - 1] = temp
    print myList
    return


revertList = [5, 6, 7, 8, 9, 0]
revert(revertList)
for x in revertList:
    print 'x:', x

# 反转韩式 revert2

revertResult = []


def revert2(myList):
    for i in range(len(myList)):
        revertResult.append(myList.pop())
    return revertResult


revertList2 = [6, 7, 8, 9, 0, 19]
revert2(revertList2)
for x in revertResult:
    print 'x====', x
