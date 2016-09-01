#! -*-coding:utf-8-*-
"""
name: 60YFK
version: 0.1 Beta
create time: 08-18-2016
author: How Peng
email: howpeng@foxmail.com
"""
import sqlite3
import hashlib
import getpass
import shelve
import time
import sys

#############################
#    登录　　　开始
#    保存用户信息的数据库为　user_db
#############################


def save_info(username, password):
    """保存用户账号信息,用shelve存储"""
    with shelve.open('users_db') as users_db:
        users_db[username] = password
        for i in users_db.keys():
            print(i + ':' + users_db[i])


def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    pass_md5 = md5.hexdigest()
    return pass_md5


def register():
    username = input("输入用户名:　")
    with shelve.open('users_db') as users_info:
        if username not in users_info.keys():
            while True:
                password_1 = getpass.getpass("输入密码:　")
                password_2 = getpass.getpass("确认密码:　")
                if password_1 == password_2:
                    password = get_md5(password_2)
                    save_info(username, password)
                    print("OK! 新用户[%s]注册成功" % username)
                    login()
                    return False
                elif password_1 != password_2:
                    print("ERROR! 两次密码不一致,请重新输入!")
                    continue
        elif username in users_info.keys():
            print("ERROR! 用户已存在,请重新输入!")
            register()


def login():
    username = input("登录账号:　")
    users_info = shelve.open('users_db')
    if username == 'r':
        register()
    elif username in users_info.keys() and username != 'r':
        password = getpass.getpass("登录密码:　")
        if users_info[username] == get_md5(password):
            print("OK! 管理员[%s]登录成功" % username)
            main()
        elif users_info[username] != get_md5(password):
            print("ERROR! 密码错误")
    elif username not in users_info and username != 'r':
        print("ERROR! 用户不存在,请重新输入!")
    users_info.close()


def show_all():
    pass



#############################
#    登录　　　结束
#############################



#############################
#    数据库操作　　　开始
#############################

def connect_database():
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    return conn, curs


def create_table(conn, curs):
    curs.execute("""create table cangku (ID int, NAME char, NUM int, TIME char)""")
    curs.execute("""create table fendui (TEAM char, NAME char, NUM int, TIME char)""")
    conn.commit()
    curs.close()

def add_record():
    """
    将提前准备好的记录录入到数据表中。
    下步考虑怎么将excel表中的数据导进来!!!!!
    """
    conn, curs = connect_database()
    first = input("新货入库(n),还是旧货补充(a)")     # BUG! 补货记录没有体现
    if first == 'n':
        id = input("id: ")
        name = input('name: ')
        num = input('number: ')
        query = 'insert into cangku values (?,?,?,?);'
        curs.execute(query, (id, name, num, time.asctime()))
        log(t='仓库', n=name, m=num, i=1)
    elif first == 'a':
        id = input("id: ")
        num = int(input('number: '))
        curs.execute("""select * from cangku where ID = ?""", (id,))
        rr = curs.fetchone()
        nn = rr[2]
        sum = nn + num
        curs.execute("""update cangku set NUM = ? where ID = ?""", (sum, id))
        log(t='仓库', n=nn, m=num, i=1)
    conn.commit()
    curs.close()


def look_for_records(n):
    conn, curs = connect_database()
    curs.execute("""select * from %s""" % n)  # 待修改成可选择显示内容
    for i in curs.fetchall():
        show_record(i)
    conn.commit()
    curs.close()

def show_record(i):
    print("序号:%s　|　品名:%s%s|　数量:%s%s　|　更新时间:%s\n%s" % (i[0], i[1], ' ' * (10 - len(i[1])), i[2], ' ' * (5 - len(str(i[2]))), i[3], '-' * 78))



def updata_records():
    conn, curs = connect_database()
    team = input("team: ")
    id = input("id: ")
    num = int(input("number: "))
    curs.execute("""select * from cangku where ID = ?""", (id,))
    record = curs.fetchone()
    n = record[2]
    name = record[1]
    sum = n - num
    curs.execute("""update cangku set NUM = ?, TIME = ? where ID = ?""", (sum, time.asctime(), id))
    curs.execute("""insert into fendui values (?,?,?,?)""", (team, name, num, time.asctime()))
    log(team, name, num)
    conn.commit()
    curs.close()


def delete_records():
    """删除记录,用字典"""
    pass

def log(t, n, m, i=0):
    """内容不全!!!!!!!!!!"""
    with open('log_file', 'a') as log_file:
        ac = ['领取', '入库']
        query = "[%s]  %s %s [%s] %s个\n" % (time.asctime(), t, ac[i], n, m)
        log_file.write(query)
        print(query)

def ck_m():
    """仓库管理操作:1)显示库存,标注出缺货物品　2)物资入库　3)生成物资补充计划"""
    cmd('ck')

def out_m():
    """出库管理,将出库详细信息记录到log中。"""
    cmd('out')

def look_for():
    """查询管理。1)可查询单位,物品指定时间内的用量
    　　　　　　　2)生成统计报表"""
    cmd('look_for')
    print("thi is a test")


def create_excel():
    """生成补充计划表"""
    pass

def go_back():
    """返回上一级菜单"""
    return False

def backup():
    """每次使用都进行备份"""
#############################
#    数据库操作　　　结束
#############################


def cmd(n):
    cmds = {'main': {'1': ck_m, '2': out_m, '3': look_for},
            'ck': {'1': show_all, '2': add_record, '3': create_excel, '4': go_back},
            'out': {},
            'look_for': {'1': look_for_records('cangku')}}
    prompt = {'main': """可用命令: \n\t(1)库存管理\n\t(2)出库操作\n\t(3)查询记录\n\t(4)返回上级菜单\n\t(e)退出程序\n请输入指令: """,
              #仓库管理
                'ck': """\n####　库存管理　####\n可用命令: \n\t(1)显示库存量\n\t(2)物资入库\n\t(3)生成补充计划\n\t(4)返回上级菜单\n\t(e)退出程序\n请输入指令: """,
              #出库操作
                'out': """\n####　出库操作　####\n可用命令: \n\t(1)请领消耗\n\t(2)临时借出\n\t(3)返回上级菜单\n\t(e)退出程序\n请输入指令: """,
              # 查询记录
              'look_for': """\n####　查询记录　####\n可用命令: \n\t(1)请领记录\n\t(2)临时借出记录\n\t(3)返回上级菜单\n\t(e)退出程序\n请输入指令: """
              }
    while True:
        i = input(prompt[n])
        if i in '1234':
            cmds[n][i]()
        elif i == 'e':
            sys.exit()
        else:
            return False


def main():
    conn, curs = connect_database()
    print("OK! 成功连接数据库")
    cmd('main')
    conn.commit()
    curs.close()

if __name__ == '__main__':
    main()


