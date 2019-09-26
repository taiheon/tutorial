
import sqlite3
conn = sqlite3.connect("sdb.db")
cur = conn.cursor()
#cur.execute("create table test (name text, score int)")
#cur.execute("insert into test values ('a',100)")
#conn.commit()

#cur.execute("insert into test values (?, ?)",('b',1))
#conn.commit()

#cur.execute("insert into test values (:name, :score)", {'name':'c','score':99})
#conn.commit()

# data=[('d',93),('e',11),('f',13)]
# cur.executemany("insert into test values (?, ?)",data)
# conn.commit()

cur.execute('select * from test')
for row in cur:
    print(row[0] , row[1])
cur.execute('select * from test')
rows = cur.fetchall()
print (rows)
conn.close()