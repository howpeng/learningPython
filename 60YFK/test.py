#! -*-coding:utf-8-*-

import sqlite3
import time

conn = sqlite3.connect('hahaha')
curs = conn.cursor()
curs.execute("""create table if not exists all_in_one (ID char, NAME char, NUM int, FF char, TT char, BEHAVE char,TIME char)""")

curs.execute("""insert into all_in_one values ('1', 'one', 100, 'store', 'cangku', 'in', '%s')""" % time.asctime())
curs.execute("""insert into all_in_one values ('1', 'one', -10, 'cangku', 'zb1l', 'out', '%s')""" % time.asctime())
curs.execute("""insert into all_in_one values ('1', 'one', -20, 'cangku', 'zb2l', 'borrow', '%s')""" % time.asctime())
curs.execute("""insert into all_in_one values ('1', 'one', 20, 'zb2l', 'cangku', 'back', '%s')""" % time.asctime())

curs.execute("""insert into all_in_one values ('1', 'one', 200, 'store', 'cangku', 'in', '%s')""" % time.asctime())
curs.execute("""insert into all_in_one values ('1', 'one', -30, 'cangku', 'zb3l', 'out', '%s')""" % time.asctime())
curs.execute("""insert into all_in_one values ('1', 'one', -20, 'cangku', 'zb2l', 'borrow', '%s')""" % time.asctime())
curs.execute("""insert into all_in_one values ('1', 'one', 20, 'zb2l', 'cangku', 'back', '%s')""" % time.asctime())

curs.execute("""insert into all_in_one values ('2', 't', 100, 'store', 'cangku', 'in', '%s')""" % time.asctime())
curs.execute("""insert into all_in_one values ('2', 't', -10, 'cangku', 'zb1l', 'out', '%s')""" % time.asctime())
curs.execute("""insert into all_in_one values ('2', 't', -20, 'cangku', 'zb2l', 'borrow', '%s')""" % time.asctime())
curs.execute("""insert into all_in_one values ('2', 't', 10, 'zb2l', 'cangku', 'back', '%s')""" % time.asctime())

#curs.execute("""select NAME, sum(NUM) from all_in_one group by NAME""")

curs.execute("""select TT, NAME, SUM(NUM) from all_in_one where BEHAVE = 'out' and NAME = 'one' group by TT""")

for i in curs.fetchall():
    print(i)