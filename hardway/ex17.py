"""
重新更改过的复制脚本
若目标文件名不存在,则直接复制
若目标文件名已存在,则提示是否继续
用法: python3 ex17.py from_file to_file
"""


from sys import argv
from os.path import exists

script, from_file, to_file = argv

def copy_file(ff=from_file, tf=to_file):
    input_file = open(from_file)
    data = input_file.read()
    output_file = open(to_file, 'w')
    output_file.write(data)
    print("已将 %s 复制到 %s 。" % (from_file, to_file))
    input_file.close()
    output_file.close()

if exists(to_file):
    a = input("已存在相同文件名文件,是否继续? (y or n)")
    if a == 'y':
        copy_file()
    else:
        print("复制已停止。")
else:
    copy_file()




