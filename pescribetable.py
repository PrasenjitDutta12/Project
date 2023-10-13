import sqlite3
conn=sqlite3.connect("dms.db")
cur=conn.cursor()
sql="create table pescribe(pid text(30),date text(20),docname text(30),symptom text(30),medicine text(30),remark text(30))"
cur.execute(sql)
'''sql="select * from pescribe sys"
res=cur.execute(sql)
s=res.fetchall()
print(s)'''
conn.commit()
conn.close()