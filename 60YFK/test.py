#! -*-coding:utf-8-*-

print("请登陆,或按回车进入其他")
u = input("user: ")
p = input("password: ")
if u != '' and p != '':
    print(u, p)
elif u == '' and p == '':
    print("hahahahha others thing to do")

