# ## connecting to database and creating a database and a table   ####
import mysql.connector
#
# # # establish connection between mysql server and python code- serever connection
# con=mysql.connector.connect(user="root",password="Bidhya",host="localhost")
# #
# # print(con) # it returns connection object
# #
# # # create  a new  cursor object - cursor used for executing qurey
# c=con.cursor()
# #
# query="create database school_db1"
# c.execute(query)
# #
# print("DataBase file created")
# c.close()
# con.close()


## create table in schooldb

con=mysql.connector.connect(user="root",password="Bidhya",host="localhost",database="school_db1")
c=con.cursor()
# c.execute("drop table student")
# query="""create table student(
#         roll_no int not null primary key,
#         name varchar(20),
#         age int,
#         place varchar(20),
#         phone varchar(20),
#         total_mark int)""";
# c.execute(query)
# print("Table Created")

# create new record or insert data into database table student

# query="insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(101,'arun',12,'ekm',1543289765,145)
# c.execute(query,data)
# con.commit() # permenently save data into database
# print("Inserted data successfully")
# c.close()
# con.close()


# read the records
#1 create or set connection
#2 give query
#3 take data and print
#4 close connection

