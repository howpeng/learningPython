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

#############################
#    登录　　　开始
#############################
db = {}

def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    pass_md5 = md5.hexdigest()
    return pass_md5

def register():
    username = input("输入用户名:　")
    if username not in db.keys():
        password_1 = getpass.getpass("输入密码:　")
        password_2 = getpass.getpass("确认密码:　")
        if password_1 == password_2:
            password = password_2
            db[username] = get_md5(password)
            print("OK! 新用户[%s]注册成功" % username)
        elif password_1 != password_2:
            print("两次密码不一致,请重新输入!")
            register()
    elif username in db.keys():
        print("用户已存在,请重新输入!")
        register()

def login(username, password):
    pass

def show_all():
    pass



#############################
#    登录　　　结束
#############################



#############################
#    数据库操作　　　开始
#############################

records = [(1, 'xujixing', 30),
           (2, 'dangxiangguo', 24),
           (3, 'shijiujian', 30),
           (4, 'qixiang', 30)]

class Prompt(object):
    tips = {'connect_database': 'OK! 连接数据库 test.db',
            'create_table': 'OK! 创建数据表 test'}


def connect_database():
    conn = sqlite3.connect('test.db')
    curs = conn.cursor()
    print(Prompt.tips['connect_database'])
    return conn, curs


def create_table(conn, curs):
    curs.execute('create table test (ID int, NAME char, AGE int)')
    print(Prompt.tips['create_table'])



def add_record(records, curs):
    """
    将提前准备好的记录录入到数据表中。
    下步考虑怎么将excel表中的数据导进来!!!!!
    :param records: 提前准备好的记录表
    :param curs:
    :return:
    """
    #id = input("ID: ")
   # name = input("NAME: ")
   # age = input("AGE: ")
   # t = (id, name, age)
    for i in records:
        curs.execute('insert into test values (?,?,?)', i)
   # print('ADD ==>\n\tID: %s\n\tNAME: %s\n\tAGE: %s' % (id, name, age))


def show_records(curs):
    curs.execute('select * from test where id = 1') # 待修改成可选择显示内容
    for i in curs.fetchall():
        print(i)

def updata_records():
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
            add_record(records, curs)
        elif i == 's':
            show_records(curs)
        elif i == 'e':
            return False
    conn.commit()
    curs.close()

if __name__ == '__main__':
    for i in range(1,4):
        register()
        print(list(db.keys()))

