import sqlite3
conn=sqlite3.connect("dms.db")
cur=conn.cursor()
'''sql="create table admin(name text(30),phno text(20),Eid text(30),password text(30))"
cur.execute(sql)'''
sql="select * from admin sys"
res=cur.execute(sql)
s=res.fetchall()
print(s)
conn.commit()
conn.close()