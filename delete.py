## delete record   ###

import mysql.connector
con=mysql.connector.connect(user="root",password="Arunima",host="localhost",database="school_db")
print(con)
c=con.cursor()


query="delete from student where roll_no=%s"
data=(101,)  ## , is used in tuple to identify it is a sequence
c.execute(query,data)
con.commit()
if c.rowcount>0:
    print("data is deleted")
else:
    print("no record found")

c.close()
con.close()