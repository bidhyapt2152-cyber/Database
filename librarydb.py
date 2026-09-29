import mysql.connector
class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="Bidhya",host="localhost",database="library_db")
        self.cursor=self.con.cursor()
        print("Successfully connected")

#     def list(self):
#         query = "select * from book"
#         self.cursor.execute (query)
#         records = self.cursor.fetchall()
#         if records:
#             for row in records:
#                 print(row)
#         else:
#             print("record not found")
#
#     def create(self,title,author,price,language,pages):
#         query="insert into book(title,author,price,language,pages) values(%s,%s,%s,%s,%s)"
#         data=(title,author,price,language,pages)
#         self.cursor.execute(query,data)
#         self.con.commit() # permenently save data into database
#         print("Inserted data successfully")
#
#
#
#
#     def retrieve(self,id):
#         query="select * from book where id=%s"
#         data=(id,)  ## , is used in tuple to identify it is a sequence
#         self.cursor.execute(query,data)
#         record=self.cursor.fetchone()  ## take one data or id- fetchone()
#         if record:
#             print(record)
#         else:
#             print("record not found")
#
#
#     def delete(self,id):
#         query="delete from book where id=%s"
#         data=(id,)  ## , is used in tuple to identify it is a sequence
#         self.cursor.execute(query, data)
#         self.con.commit()
#         if self.cursor.rowcount > 0:
#             print("data is deleted")
#         else:
#             print("no record found")
#     def update(self,title,author,price,language,pages,id):
#         query = "update book set title=%s,author=%s,price=%s,language=%s,pages=%s where id=%s"
#         data = (title,author,price,language,pages,id)
#         self.cursor.execute(query,data)
#         self.con.commit()
#         if self.cursor.rowcount > 0:
#             print("data is updated")
#         else:
#             print("no record found")
#
#
#
b=BookListCreateRetrieveUpdateDelete()
# b.list()
# b.create('book2','renu',400,'malayalam',380)
# b.retrieve(2)
# b.delete(2)
# b.update('book3','hari',500,'english',450,3)