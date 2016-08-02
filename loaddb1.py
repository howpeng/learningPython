#! -*-coding:utf-8-*-

import sqlite3
conn = sqlite3.connect('dbase1')
curs = conn.cursor()
curs.execute('create table people (name char, job char, pay int)')
file = open('data1.txt')
rows = [line.rstrip().split(', ') for line in file]
for rec in rows:
    curs.execute('insert into people values (?,?,?)', rec)

conn.commit()
conn.close()

