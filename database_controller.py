import mysql.connector as mysql

host = "hms.cm10enqi961k.us-east-2.rds.amazonaws.com"
user = "admin"
password = "44966874"

class Database:
    def __init__(self):
        """
        # Connecting to mysql database
        try:
            self.db = mysql.connect(host=host,
                                    user=user,
                                    password=password)
            print("Connected successfully")
        except Exception as e:
            print("Failed to connect")
            print(e)

        # Creating lmsdatabase
        try:
            self.mycursor = self.db.cursor()
            self.mycursor.execute("CREATE DATABASE lmsdatabase")
            print("lmsdatabase has been created")
        except Exception as e:
            print("Could not create database")
            print(e)"""

        # Connecting to lmsdatabase
        try:
            self.db1 = mysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database="lmsdatabase")
            print("Connected to lmsdatabase")
        except Exception as e:
            print("Could not connect to lmsdatabase")
            print(e)