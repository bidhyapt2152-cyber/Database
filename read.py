###   read all records from a table   ###


import mysql.connector
con=mysql.connector.connect(user="root",password="Arunima",host="localhost",database="school_db")
print(con)
c=con.cursor()


query="select * from student"

c.execute(query)
records=c.fetchall()
if records:
    for row in records:
        print(row)
else:
    print("record not found")

c.close()
con.close()