import pymongo

client = pymongo.MongoClient('localhost', 27017)
dbdb = client['dbdb']
sheet_tab = dbdb['sheet_tab']
"""
path = '/Users/heropeng/Desktop/dd.txt'
with open(path, 'r') as f:
    lines = f.readlines()
    for index, line in enumerate(lines):
        data = {
            'index': index,
            'line': line,
            'words': len(line.split())
        }
        sheet_tab.insert_one(data)
"""
for item in sheet_tab.find({'words':{'$gt':5}}):
    print(item)