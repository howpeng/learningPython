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
    curs.execute("""create table if not exists records (ID char,
                                          NAME char,
                                          MODEL char,
                                          NUM int,
                                          FF char,
                                          TT char,
                                          BEHAVE char,
                                          TIME char)""")
    conn.commit()
    curs.close()


def delete_records():
    """删除记录,用字典"""
    pass


def log(company, i, name, model, number):
    """时间,单位,行为,物品,规格,数量"""
    behave = ['入库', '领取', '借出', '归还']
    with open('log_file', 'a') as log_file:
        query = "%s | %s %s %s 型号%s %s个;\n" % (time.asctime(), company, behave[i], name, model, number)
        log_file.write(query)
        print(query)


def ck_m():
    """仓库管理操作:1)显示库存,标注出缺货物品　2)物资入库　3)生成物资补充计划"""
    cmd('ck')


def out_m():
    """出库管理,将出库详细信息记录到log中。"""
    cmd('out')


def show():
    """查询管理。1)可查询单位,物品指定时间内的用量
    　　　　　　　2)生成统计报表"""
    cmd('show')
    print("thi is a test")


def go_back():
    """返回上一级菜单"""
    cmd('main')


def backup():
    """每次使用都进行备份"""


###############   0908更新
def show_all():  # 已进行初步测试,还需要整体测试
    conn, curs = connect_database()
    curs.execute("""select  ID, NAME, MODEL, SUM(NUM), TIME from records group by ID""")
    for i in curs.fetchall():
        print("""-- 编号:%s  |  品名:%s  |  规格:%s  |  数量:%s  |  时间:%s\n%s""" % (i[0], i[1], i[2], i[3], i[4],'-'*80))
    conn.commit()
    curs.close()


def updata_records_in():
    """待实现输入编号后自动输入品名,也就是不需要手动输入name"""
    try:
        conn, curs = connect_database()
        id, name, model, num = input("请依次输入编号、名称、型号、数量,中间以空隔分隔:\n>>>").split()
        curs.execute("""insert into records values (?,?,?,?,?,?,?,?)""", (id, name, model, num, 'store', 'cangku', 'in', time.asctime()))
        log('cangku', 0, name, model, num)
        conn.commit()                         #???????   行不行 需要不需要加finally
        curs.close()
    except ValueError:
        print('参数输入错误,请重新输入!')



def create_excel():
    pass


def update_records_out():
    """待实现输入编号后自动输入品名,也就是不需要手动输入name"""
    try:
        conn, curs = connect_database()
        company, id, name, model, num = input("请依次输入领取单位、编号、名称、型号、数量,中间以空隔分隔:\n>>>").split()
        curs.execute("""insert into records values (?,?,?,?,?,?,?,?)""",
                     (id, name, model, -int(num), 'cangku', company, 'out', time.asctime()))
        log(company, 1, name, model, num)
        conn.commit()
        curs.close()
    except ValueError:
        print("参数输入错误,请重新输入!")


def borrow_temp():
    """待实现输入编号后自动输入品名,也就是不需要手动输入name"""
    try:
        conn, curs = connect_database()
        company, id, name, model, num = input("请依次输入借出单位、编号、名称、型号、数量,中间以空隔分隔:\n>>>").split()
        curs.execute("""insert into records values (?,?,?,?,?,?,?,?)""",
                     (id, name, model, -int(num), 'cangku', company, 'borrow', time.asctime()))
        log(company, 2, name, model, num)
        conn.commit()
        curs.close()
    except ValueError:
        print("参数输入错误,请重新输入!")


def back_temp():
    """待实现输入编号后自动输入品名,也就是不需要手动输入name"""
    try:
        conn, curs = connect_database()
        company, id, name, model, num = input("请依次输入借出单位、编号、名称、型号、数量,中间以空隔分隔:\n>>>").split()
        curs.execute("""insert into records values (?,?,?,?,?,?,?,?)""",
                     (id, name, model, num, company, 'cangku', 'back', time.asctime()))
        log(company, 3, name, model, num)
        conn.commit()
        curs.close()
    except ValueError:
        print("参数输入错误,请重新输入!")


def show_out():
    conn, curs = connect_database()
    company = input("请输入要查询的单位: ")
    curs.execute("""select TT, ID, NAME, MODEL, SUM(NUM), TIME from records where BEHAVE = 'out' and TT = ? group by ID """, (company,))
    for i in curs.fetchall():
        print("""-- 单位:%s  |  编号:%s  |  品名:%s  |  规格:%s  |  数量:%s  |  时间:%s\n%s""" % (i[0], i[1], i[2], i[3], -int(i[4]), i[5], '-' * 100))
    conn.commit()
    curs.close()


def show_borrow():
    """需要增加一个选择: 显示全部借出物品,或是选择借出单位"""
    conn, curs = connect_database()
    company = input("请输入要查询的单位: ")
    curs.execute(
        """select TT, ID, NAME, MODEL, SUM(NUM), TIME from records where BEHAVE = 'borrow' and TT = ? group by ID """,
        (company,))
    for i in curs.fetchall():
        print("""-- 单位:%s  |  编号:%s  |  品名:%s  |  规格:%s  |  数量:%s  |  时间:%s\n%s""" % (
        i[0], i[1], i[2], i[3], i[4], i[5], '-' * 80))
    conn.commit()
    curs.close()


def show_back():
    """需要增加一个选择: 显示全部借出物品,或是选择借出单位"""
    conn, curs = connect_database()
    company = input("请输入要查询的单位: ")
    curs.execute(
        """select TT, ID, NAME, MODEL, SUM(NUM), TIME from records where BEHAVE = 'back' and FF = ? group by ID """,
        (company,))
    for i in curs.fetchall():
        print("""-- 单位:%s  |  编号:%s  |  品名:%s  |  规格:%s  |  数量:%s  |  时间:%s\n%s""" % (
        i[0], i[1], i[2], i[3], i[4], i[5], '-' * 80))
    conn.commit()
    curs.close()


def show_log():
    with open('log_file') as f:
        for i in f.readlines():
            print(i)

#############################
#    数据库操作　　　结束
#############################


def cmd(n):
    """菜单选择函数"""
    CMDs = {'main': {'1': ck_m, '2': out_m, '3': show, '4': go_back},
            'ck': {'1': show_all, '2': updata_records_in, '3': back_temp, '4': create_excel, '5': go_back},
            'out': {'1': update_records_out, '2': borrow_temp, '3': go_back},
            'show': {'1': show_out, '2': show_borrow, '3': show_back, '4': show_log, '5': go_back}}
    prompt = {'main': """\n####  功能菜单  ####\n可用命令: \n\t(1)库存管理\n\t(2)出库操作\n\t(3)查询记录\n\t(4)返回上级菜单\n\t(e)退出程序\n请输入指令: """,
              #仓库管理
                'ck': """\n####　库存管理　####\n可用命令: \n\t(1)显示库存量\n\t(2)物资入库\n\t(3)物资归还\n\t(4)生成补充计划\n\t(5)返回上级菜单\n\t(e)退出程序\n请输入指令: """,
              #出库操作
                'out': """\n####　出库操作　####\n可用命令: \n\t(1)请领消耗\n\t(2)临时借出\n\t(3)返回上级菜单\n\t(e)退出程序\n请输入指令: """,
              # 查询记录
              'show': """\n####　查询记录　####\n可用命令: \n\t(1)请领记录\n\t(2)临时借出记录\n\t(3)归还记录\n\t(4)操作日志\n\t(5)返回上级菜单\n\t(e)退出程序\n请输入指令: """
              }
    while True:
        try:
            i = input(prompt[n])
            if i in '12345':
                CMDs[n][i]()
            elif i == 'e':
                sys.exit()
        except KeyError:
            print("没有此命令,请重新输入!")





def main():
    conn, curs = connect_database()
    create_table(conn, curs)
    print("OK! 成功连接数据库")
    cmd('main')
    conn.commit()
    curs.close()

if __name__ == '__main__':
    login()



