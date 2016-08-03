# -- coding:utf-8 --

from sys import argv

script, user_name, age = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I know you are %s years old." % age)
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("you said %s about liking me." % likes)