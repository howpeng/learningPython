#! -*- coding:utf-8 -*-
import shelve
import initdata

i = input("What do You want to do? \nInitial(i)   Add(a)\nShowAll(s)   Exit(e)\n===> ")

if i == 'i':
    db = shelve.open('demo01-test-file')
    db.close()
elif i == 's':
    db = shelve.open('demo01-test-file')
    print(list(db))
    db.close()