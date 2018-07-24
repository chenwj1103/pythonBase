#!/usr/bin/python
# -*- coding: utf-8 -*-


import MySQLdb

db = MySQLdb.connect("localhost", "root", "root", "pythonDB", charset='utf8')

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """ CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

db.close()
