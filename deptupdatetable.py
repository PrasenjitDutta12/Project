import sqlite3
conn=sqlite3.connect("dms.db")
cur=conn.cursor()
'''sql="create table deptupdatetable(Name text(20))"
cur.execute(sql)'''

sql="select * from deptupdatetable "
res=cur.execute(sql)
r=res.fetchall()
print(r)
conn.commit()
conn.close()