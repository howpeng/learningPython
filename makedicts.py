#! -*-coding:utf-8-*-

"""
转化元组的列表为行字典的列表,用字段名作为键名
这不是命令行实用工作:如果运行,会运行dgqj编码的自测试
"""

def makedicts(cursor, query, params=()):
    corsor.execute(query, params)
    colnames = [desc[0] for desc in cursor.description]
    rowdicts = [dict(zip(colnames, row)) for row in cursor.fetchall()]
    return rowdicts

if __name__ == '__main':
    import sqlite3
    conn = sqlite3.connect('dbase1')
    cursor = conn.cursor()
    query = 'select name, pay from people where pay < ?'