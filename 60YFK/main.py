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
#############################
#    登录　　　开始
#############################


def save_info(username, password):
    """保存用户账号信息,用shelve存储"""
    with shelve.open('users_info') as users_db:
        users_db[username] = password
        for i in users_db.keys():
            print(i + ':' + users_db[i])


def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    pass_md5 = md5.hexdigest()
    return pass_md5

def register():                                         # !!!有ＢＵＧ!!!!!!!!!!!
    username = input("输入用户名:　")
    with shelve.open('users_db') as users_info:
        if username not in users_info.keys():
            password_1 = getpass.getpass("输入密码:　")
            password_2 = getpass.getpass("确认密码:　")
            if password_1 == password_2:
                password = get_md5(password_2)
                save_info(username, password)
                print("OK! 新用户[%s]注册成功" % username)
            elif password_1 != password_2:
                print("ERROR! 两次密码不一致,请重新输入!")
                register()
        elif username in users_info.keys():
            print("ERROR! 用户已存在,请重新输入!")
            register()

def login():
    username = input("登录账号:　")
    with shelve.open('users_db') as users_info:
        if username in users_info.keys():
            password = getpass.getpass("登录密码:　")
            if users_info[username] == get_md5(password):
                print("OK! 管理员[%s]登录成功" % username)
            elif users_info[username] != get_md5(password):
                print("ERROR! 密码错误")
                login()
        elif username not in users_info.keys():
            print("ERROR! 账号不存在")
            register()


def show_all():
    pass



#############################
#    登录　　　结束
#############################



#############################
#    数据库操作　　　开始
#############################


class Prompt(object):
    tips = {'connect_database': 'OK! 连接数据库 test.db',
            'create_table': 'OK! 创建数据表 test'}


def connect_database():
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    print(Prompt.tips['connect_database'])
    return conn, curs


def create_table(conn, curs):
    curs.execute('create table cangku (编号 int primary key, 品名 char, 数量 int,时间 char)')
    print(Prompt.tips['create_table'])
    conn.commit()
    curs.close()



def add_record(conn, curs):
    """
    将提前准备好的记录录入到数据表中。
    下步考虑怎么将excel表中的数据导进来!!!!!
    """
    conn, curs = connect_database()
    curs.execute("insert into cangku values (001, '水龙头', 100, '2016-08-23')")
    curs.execute("insert into cangku values (002, '三通', 100, '2016-08-23')")
    curs.execute("insert into cangku values (003, '活接', 100, '2016-08-23')")
    curs.execute("insert into cangku values (004, '阀门', 100, '2016-08-23')")
    conn.commit()
    curs.close()


def show_records(curs):
    curs.execute('select * from cangku') # 待修改成可选择显示内容
    for i in curs.fetchall():
        print(i)

def updata_records(conn, curs):

    pass

#############################
#    数据库操作　　　结束
#############################

def main():
    conn, curs = connect_database()
    while True:
        i = input("可用命令: (a)添加记录,　(s)显示记录,　(e)退出程序\n请输入指令: ")
        if i == 'c':
            create_table(conn, curs)
        elif i == 'a':
            add_record(conn, curs)
        elif i == 's':
            show_records(curs)
        elif i == 'e':
            return False
    conn.commit()
    curs.close()

if __name__ == '__main__':
    main()

