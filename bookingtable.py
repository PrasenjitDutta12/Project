import sqlite3
conn=sqlite3.connect("dms.db")
cur=conn.cursor()
# sql="drop table booking"
#sql="create table booking(pid int,doctor text(20),symptom text(30),date date)"
#cur.execute(sql)

sql="select * from booking"
sql="select * from booking"
sql="delete from booking"
'''res=cur.execute(sql)
s=res.fetchall()
print(s)'''
conn.commit()
conn.close()