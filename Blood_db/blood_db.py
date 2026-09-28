# Blood Donor Management System using Python, MySQL and Streamlit
# Create a MySQL database named blood_db and create a table named donor to store blood donor details.
# The donor table should contain the following fields:
# id – Integer, Primary Key, Auto Increment
# name – Donor name
# bloodgroup – Blood group
# phone – Phone number, should be unique
# city – City
# last_donation – Date of last donation
# Create a Python class to perform database operations on the donor table.
# The class should contain methods to:
# Add a new donor
# Retrieve all donors
# Retrieve a donor using ID
# Update donor details
# Delete a donor using ID
# Create a Streamlit interface to perform these operations through a user-friendly interface.


import mysql.connector

class DonarCRUD:
    def __init__(self):    ###### instead of giving connection to every class call, connection is defined in init function
        self.connection=mysql.connector.connect(user="root",password="root",host="localhost",
                                                database="blood_db")
        print(self.connection)
        self.cursor=self.connection.cursor()    ##in cursor definition 'self' is needed

        print("SUCCESSFULLY CONNECTED")

    def get(self):
        # reading all records from db table
        query="select * from donar"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            # for row in records:
                # print(row)
            return records
        else:
            # print("NO RECORDS FOUND")
            return False

    def post(self,name,bloodgroup,phone,city,last_donation):
        query="insert into donar(name,bloodgroup,phone,city,last_donation)values(%s,%s,%s,%s,%s)"
        data=(name,bloodgroup,phone,city,last_donation)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("DATA INSERTED SUCCESSFULLY")

    def retrieve(self,id):
        query="select * from donar where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            # print(record)
            return record
        else:
            print("NO RECORDS FOUND")

    def put(self,name,bloodgroup,phone,city,last_donation,id):
        query="update donar set name=%s,bloodgroup=%s,phone=%s,city=%s,last_donation=%s where id=%s"
        data=(name,bloodgroup,phone,city,last_donation,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            # print("DATA UPDATED SUCCESSFULLY")
            return True
        else:
            # print("NO RECORDS FOUND")
            return False

    def delete(self,id):
        query="delete from donar where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            # print("DATA IS DELETED")
            return True
        else:
            # print("NO RECORDS FOUND")
            return False

