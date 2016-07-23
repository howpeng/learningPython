# -*- coding:utf-8 -*-
from name_base import danwei, pinming
import sys, shelve
'''
{仓库:　{品名1:　数量,　品名2:　数量...}}
先可以输入初始的库存,再通过update_inventory()进行更新
'''
def store_data(db):
    pid = input("单位代号: ")
    material = {}
    name = input("品名: ")
    material[pinming[name]] = int(input("数量: "))
    db[pid] = material

def update_material(db):
    '''已有物品就是增减变化,没有的就是增加新物品'''
    pid = input("单位代号: ")
    new_m = input("品名: ")
    new_n = int(input("数量: "))
    t = db[pid]
    t[pinming[new_m]] += new_n
    db[pid] = t





def lookup_person(db):
    pid = input("单位代号: ")
    print(danwei[pid], '==> ', db[pid])

def enter_command():
    cmd = input("更新(a)、显示(l)、退出(q)\n输入命令: ")
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
            elif cmd == 'a':
                update_material(database)
            elif cmd == 'q':
                print("程序已退出!")
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()