import sqlite3

def convert(value):
    if value.startswith("~"):
        return value.strip("~")
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE food (
id          TEXT    primary key,
desc        text,
water       float,
kcal        float,
protein     float,
fat         float,
ash         float,
carbs       float,
fiber       float,
sugar       float)''')

query = 'insert into food values (?,?,?,?,?,?,?,?,?,?)'

for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()
