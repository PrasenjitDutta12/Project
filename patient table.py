import sqlite3
conn=sqlite3.connect("dms.db")
cur=conn.cursor()
'''sql="create table patient(pid int,name text(30),phno text(20),Eid text(30),Address text(30),gender text(30),bloodgroup text(30))"
cur.execute(sql)
sql="select * from patient "'''
'''sql="drop table patient"'''
'''sql = "INSERT INTO patient(pid, name, phno, Eid, Address, gender, bloodgroup) VALUES (?, ?, ?, ?, ?, ?, ?)"
values = ("P001", "sanu", "1234567890", "121.com", "123 street", "Male", "o+")
cur.execute(sql,values)'''
'''sql="delete from patient"'''
sql="select * from patient"
res=cur.execute(sql)
s=res.fetchall()
print(s)
conn.commit()
conn.close()