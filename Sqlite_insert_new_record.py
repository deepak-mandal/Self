#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:27:11 2020

@author: deepak
"""


import sqlite3
MySchool=sqlite3.connect('schooltest.db')
curschool=MySchool.cursor()
mysid=int(input('Enter ID: '))
myname=input('Enter name: ')
myhouse=int(input('Enter house: '))
mymarks=float(input('Enter marks: '))

curschool.execute('''insert into students(syudentID, name, house, marks)
                  values (?, ?, ?, ?);''', (mysid, myname, myhouse, mymarks))
MySchool.commit()


