#! -*-coding:utf-8-*-
"""
name: 60YFK
version: 0.1 Beta
create time: 08-18-2016
author: How Peng
email: howpeng@foxmail.com
"""
import sqlite3

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
    conn.commit()
    curs.close()
    print(Prompt.tips['create_table'])



def add_record(records, curs):
    """
    将提前准备好的记录录入到数据表中。
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
    main()