
            # ======== LIBRARY_DB ========


# Define a class to perform database operations on Book table

# create a class named BookListCreateRetrieveUpdateDelete
# and define methods:
# list() -->for reading all records
# create() -->for creating a new record
# retrieve() -->for reading a specific record
# update(id,data) -->for updating a specific record
# delete(id) -->for deleting a specific record

import mysql.connector

class BookListCreateRetrieveUpdateDelete:

    def __init__(self):        ### instead of giving connection to every class call, connection is defined in init fn
        self.connection= mysql.connector.connect(user="root", password="root", host="localhost", database="library_db")
        print(self.connection)
        self.cursor = self.connection.cursor()          ### in cursor definition 'self' is needed
        print("SUCCESSFULLY CONNECTED")

    def list(self):
        # reading all records from db table
        query="select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            # for row in records:
                # print(row)
            return records
        else:
            print("NO RECORDS FOUND")

    def create(self,title,author,price,pages,language):
        query="insert into book(title,author,price,pages,language)values(%s,%s,%s,%s,%s)"
        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("DATA INSERTED SUCCESSFULLY")

    def retrieve(self,id):
        query="select * from book where id=%s"
        data=(id,)              ### if only one element then we should use ' , ' otherwise it shows error
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            # print(record)
            return record
        else:
            print("NO RECORDS FOUND")

    def update(self,title,author,price,pages,language,id):
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data=(title,author,price,pages,language,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:              ### Gives the number of rows affected by the query.
            # print("DATA UPDATED SUCCESSFULLY")
            return True
        else:
            # print("NO RECORDS FOUND")
            return False

    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:          ### if no updations rowcount returns 0
            # print("DATA IS DELETED")
            return True
        else:
            # print("NO RECORDS FOUND")
            return False

                ### We put the database connection inside __init__() so that the connection is created automatically when the object is created.
                ### We don't have to write the connection code again and again inside list(), create(), update(), etc.

book_instance=BookListCreateRetrieveUpdateDelete()

# book_instance.list()
# book_instance.create("BOSS","Alfred",500,300,"English")
# book_instance.retrieve(2)
# book_instance.delete(1)
book_instance.update("SIGN","Emily",400,450,"English",2)



