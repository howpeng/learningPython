# -*- coding:utf-8 -*-

import sys, shelve
'''
{仓库:　{品名1:　数量,　品名2:　数量...}}
先可以输入初始的库存,再通过update_inventory()进行更新
'''
def store_data(db):
    pid = input("Enter your ID: ")
    material = {}
    name = input("Material name: ")
    material[name] = int(input("Enter the number: "))
    db[pid] = material

#def update_inventory(db):




def lookup_person(db):
    pid = input("Enter your ID: ")
    for key in db:
        print(key, '==> ', db[key])

def enter_command():
    cmd = input("Enter command: ")
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('database.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 's':
                store_data(database)
            elif cmd == 'l':
                lookup_person(database)
            elif cmd == 'q':
                return
    finally:
        database.close()

if __name__ == '__main__':
    if __name__ == '__main__':
        main()