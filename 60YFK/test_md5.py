import hashlib
import getpass

db = {}

def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    pass_md5 = md5.hexdigest()
    return pass_md5



def register(username, password):
    """还需要进行用户的分组,分为一般用户和系统管理员。"""
    db[username] = get_md5(password)

def login(username, password):
    pass

def show_users():
    print("显示所用注册用户:")
    for i in db.keys():
        print(i)
    print("显示完毕,共有%s位用户。" % len(db.keys()))

def delete_user():
    """删除用户之前要进行身份验证,只有系统管理员可以删除用户。"""
    pass

def main():
    while True:
        behave = input("Enter your command: ")
        if behave == 'r':
            username = input("username: ")
            password = getpass.getpass("password: ")   #　在IDE环境中会报错,不过在实际使用时正常
            register(username, password)
            print('OK! 新用户:' + username + '　注册成功!')
        elif behave == 's':
            show_users()

if __name__ == '__main__':
    main()