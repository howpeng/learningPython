#! -*-coding:utf-8 -*-
person = {}
db = []



def ask():
    print("\n---------------------------\nADD(a), SHOW(s), EXIT(e)\n")
    i = input("=====> ")
    if i == 'a':
        new_one()
    elif i == 's':
        print(db)
    elif i == 'e':
        return False

def new_one():
    a = input('tell me your name: ')
    b = input('how old are you? ')
    person['name'] = a
    person['age'] = b
    db.append(person)

while True:
    ask()
