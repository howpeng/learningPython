# -*- coding:utf-8 -*-
from name_base import danwei, pinming
import sys, shelve
'''
{仓库:　{品名1:　数量,　品名2:　数量...}}
先可以输入初始的库存,再通过update_inventory()进行更新
'''
def store_data(db):
    #pid = input("单位代号: ")
    #material = {}
    #name = input("品名: ")
    #material[name] = int(input("数量: "))
    #db[pid] = material
    []

def update_material(db):
    '''已有物品就是增减变化,没有的就是增加新物品'''
    pid = input("单位代号: ")
    new_m = input("品名: ")
    new_n = int(input("数量: "))
    if new_m in db[pid]:           # 假设已有该物品,直接进行数量变化
        t = db[pid]
        t[new_m] += new_n
        db[pid] = t
    elif new_m not in db[pid]:     # 仓库里之前没有该物品,添加新品名
        t = db[pid]
        t[new_m] = new_n
        db[pid] = t






def lookup(db):
    pid = input('显示指定单位(s):\n===> ')
    if pid == 'a':                                   # 全部显示
        for j in list(db.items()):
            print(j[0], '==>', j[1])
            print('-'*52)
    else:                                            # 显示指定单位
        print('-'*52)
        print(pid, '==> ', db[pid])
        print('-'*52)

def enter_command():
    cmd = input("更新(u)、显示(l)、退出(q)\n输入命令: ")
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
                lookup(database)
            elif cmd == 'u':
                update_material(database)
            elif cmd == 'q':
                print("谢谢使用\n程序已退出!")
                return
    finally:
        database.close()


if __name__ == '__main__':
    print("---------------------------------\n欢迎使用-60YFK-仓库管理系统(Alpha)\n---------------------------------")
    main()