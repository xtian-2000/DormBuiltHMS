import mysql.connector as mysql

host = "hms.cm10enqi961k.us-east-2.rds.amazonaws.com"
user = "admin"
password = "44966874"


class Database:
    def __init__(self):
        super().__init__()

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
            self.mycursor.execute("CREATE DATABASE hmsdatabase")
            print("hmsdatabase has been created")
        except Exception as e:
            print("Could not create database")
            print(e)

        # Connecting to hmsdatabase
        try:
            self.db1 = mysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     database="hmsdatabase")
            print("Connected to hmsdatabase")
        except Exception as e:
            print("Could not connect to hmsdatabase")
            print(e)

        # Creating admin table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE `hmsdatabase`.`admin` ( `admin_id` INT NOT NULL AUTO_INCREMENT,"
                                  "`username` VARCHAR(45) NOT NULL,`password` VARCHAR(45) NOT NULL,`email` VARCHAR(45)"
                                  " NOT NULL,PRIMARY KEY (`admin_id`), UNIQUE INDEX `admin_id_UNIQUE` (`admin_id` ASC)"
                                  " VISIBLE, UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE, UNIQUE INDEX"
                                  " `email_UNIQUE` (`email` ASC) VISIBLE);")
            print("'Admin' table is created successfully")
        except Exception as e:
            print("'Admin' table could not be created")
            print(e)









