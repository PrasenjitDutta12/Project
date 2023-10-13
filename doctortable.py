import sqlite3
conn=sqlite3.connect("dms.db")
cur=conn.cursor()
'''sql="create table adddoctor(name text(30),phno text(20),Eid text(30),password text(30), dept text(30))"
sql="DROP TABLE adddoctor"
cur.execute(sql)'''
sql="select * from adddoctor "
res=cur.execute(sql)
s=res.fetchall()
print(s)

conn.commit()
conn.close()