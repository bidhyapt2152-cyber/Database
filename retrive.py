##        reterieve single record      #####


import mysql.connector
con=mysql.connector.connect(user="root",password="Arunima",host="localhost",database="school_db")
print(con)
c=con.cursor()


query="select * from student where roll_no=%s"
data=(101,)  ## , is used in tuple to identify it is a sequence
c.execute(query,data)
record=c.fetchone()  ## take one data or id- fetchone()
if record:
    print(record)
else:
    print("record not found")

c.close()
con.close()