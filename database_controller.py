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

        # ================================================ admin table =================================================

        # Creating admin table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`admin` (`admin_id` INT NOT NULL "
                                  "AUTO_INCREMENT, `username` VARCHAR(45) NOT NULL, `password` VARCHAR(45) NOT NULL, "
                                  "`email` VARCHAR(45) NOT NULL, `date_created` VARCHAR(45) NOT NULL, PRIMARY KEY "
                                  "(`admin_id`), UNIQUE INDEX `admin_id_UNIQUE` (`admin_id` ASC) VISIBLE, UNIQUE INDEX "
                                  "`username_UNIQUE` (`username` ASC) VISIBLE, UNIQUE INDEX `email_UNIQUE` "
                                  "(`email` ASC) VISIBLE);")
            print("'Admin' table is created successfully")
        except Exception as e:
            print("'Admin' table could not be created")
            print(e)

        # Alter admin table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`admin` ADD COLUMN `time_created` VARCHAR(45) NOT NULL "
                                  "AFTER `date_created`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter admin table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`admin`CHANGE COLUMN `password` `password` VARCHAR(64) "
                                  "NOT NULL ;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # ================================================ basic_user table ============================================

        # Creating basic_user table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`basic_user` (`basic_user_id` INT NOT NULL "
                                  "AUTO_INCREMENT, `admin_id` INT NOT NULL, `username` VARCHAR(45) NOT NULL, "
                                  "`password` VARCHAR(45) NOT NULL, `role` VARCHAR(45) NOT NULL, `date_created` "
                                  "VARCHAR(45) NOT NULL, PRIMARY KEY (`basic_user_id`), UNIQUE INDEX "
                                  "`basic_user_id_UNIQUE` (`basic_user_id` ASC) VISIBLE, UNIQUE INDEX `username_UNIQUE`"
                                  "(`username` ASC) VISIBLE);")
            print("'basic_user' table is created successfully")
        except Exception as e:
            print("'basic_user' table could not be created")
            print(e)

        # Creating foreign key for admin_id
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`basic_user` ADD INDEX `admin_id_idx` (`admin_id` ASC) "
                                  "VISIBLE; ; ALTER TABLE `hmsdatabase`.`basic_user` ADD CONSTRAINT `admin_id` "
                                  "FOREIGN KEY (`admin_id`) REFERENCES `hmsdatabase`.`admin` (`admin_id`) ON DELETE NO "
                                  "ACTION ON UPDATE NO ACTION;")
            print("Foreign key is created")
        except Exception as e:
            print("Foreign key could not be created")
            print(e)

        # Alter basic_user table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`basic_user` ADD COLUMN `time_created` VARCHAR(45) "
                                  "NOT NULL AFTER `date_created`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # ================================================ room table ==================================================

        # Creating room table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`room` (`room_id` INT NOT NULL "
                                  "AUTO_INCREMENT, "
                                  "`room_number` INT NOT NULL, `room_description` VARCHAR(45) NULL, `room_type` "
                                  "VARCHAR(45) NULL, `room_availability` VARCHAR(45) NOT NULL, `room_capacity` INT "
                                  "NOT NULL, `admin_id` INT NOT NULL, PRIMARY KEY (`room_id`), UNIQUE INDEX "
                                  "`room_id_UNIQUE` (`room_id` ASC) VISIBLE, UNIQUE INDEX `room_number_UNIQUE` "
                                  "(`room_number` ASC) VISIBLE);")
            print("'room' table is created successfully")
        except Exception as e:
            print("'room' table could not be created")
            print(e)

        # Creating foreign key for admin_id in room
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`room` ADD INDEX `admin_id_idx` (`admin_id` ASC) "
                                  "VISIBLE;; ALTER TABLE `hmsdatabase`.`room` ADD CONSTRAINT `admin_id` FOREIGN KEY "
                                  "(`admin_id`) REFERENCES `hmsdatabase`.`admin` (`admin_id`) ON DELETE NO ACTION "
                                  "ON UPDATE NO ACTION;")
            print("Foreign key is created")
        except Exception as e:
            print("Foreign key could not be created")
            print(e)

        # Add room price column to the room table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`room` ADD COLUMN `room_price` INT NULL AFTER `admin_id`;")
            print("Price column is added to the room table successfully")
        except Exception as e:
            print("Price column could not be created successfully")
            print(e)

        # Add current_occupants column to the room table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`room` ADD COLUMN `current_occupants` INT NOT NULL "
                                  "AFTER `room_price`;")
            print("current_occupants column is added to the room table successfully")
        except Exception as e:
            print("current_occupants column could not be created successfully")
            print(e)

        # Add current_occupants column to the room table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`room` CHANGE COLUMN `room_price` `room_price` INT "
                                  "NULL DEFAULT 0 ;")
            print("alter room_price column is added to the room table successfully")
        except Exception as e:
            print("alteration could not be created successfully")
            print(e)

        # Add amenities_price column to the room table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`room` ADD COLUMN `amenities_price` INT NULL DEFAULT "
                                  "'0' AFTER `current_occupants`;")
            print("alter amenities_price column is added to the room table successfully")
        except Exception as e:
            print("alteration could not be created successfully")
            print(e)

        # Alter room table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`room` DROP INDEX `room_number_UNIQUE` ;;")
            print("Alteration is added successfully")
        except Exception as e:
            print("Alteration is not added successfully")
            print(e)

        # Alter room table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`room` ADD COLUMN `deleted` VARCHAR(45) NOT NULL DEFAULT "
                                  "'False' AFTER `amenities_price`;")
            print("Alteration is added successfully")
        except Exception as e:
            print("Alteration is not added successfully")
            print(e)

        # ================================================ tenant table ================================================

        # Creating tenant's table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`tenant` (`tenant_id` INT NOT NULL "
                                  "AUTO_INCREMENT, "
                                  "`tenant_name` VARCHAR(45) NOT NULL, `tenant_balance` VARCHAR(45) NULL, "
                                  "`date_created` VARCHAR(45) NOT NULL, `admin_id` VARCHAR(45) NOT NULL, PRIMARY KEY "
                                  "(`tenant_id`), UNIQUE INDEX `tenant_id_UNIQUE` (`tenant_id` ASC) VISIBLE, "
                                  "UNIQUE INDEX `tenant_name_UNIQUE` (`tenant_name` ASC) VISIBLE);")
            print("'tenant' table is created successfully")
        except Exception as e:
            print("'tenant' table could not be created")
            print(e)

        # Alter tenant table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`tenant` CHANGE COLUMN `date_created` `date_created` "
                                  "VARCHAR(45) NOT NULL AFTER `tenant_name`, CHANGE COLUMN `tenant_balance` "
                                  "`tenant_balance` INT NULL DEFAULT NULL , CHANGE COLUMN `admin_id` `admin_id` INT "
                                  "NOT NULL ;")
            print("Alteration is added successfully")
        except Exception as e:
            print("Alteration is not added successfully")
            print(e)

        # Alter tenant table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`tenant` ADD COLUMN `tenant_email` VARCHAR(45) NULL "
                                  "AFTER `admin_id`;")
            print("Alteration is added successfully")
        except Exception as e:
            print("Alteration is not added successfully")
            print(e)

        # Alter tenant table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`tenant` ADD COLUMN `tenant_status` VARCHAR(45) NOT NULL "
                                  "AFTER `tenant_balance`;")
            print("Alteration is added successfully")
        except Exception as e:
            print("Alteration is not added successfully")
            print(e)

        # Alter tenant table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`tenant` ADD COLUMN `room_id` INT NULL AFTER "
                                  "`tenant_email`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter tenant table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`tenant` CHANGE COLUMN `room_id` `room_id` INT NULL "
                                  "DEFAULT None ;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter tenant table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`tenant` ADD COLUMN `time_created` VARCHAR(45) NOT NULL "
                                  "AFTER `date_created`, CHANGE COLUMN `date_created` `date_created` VARCHAR(45) NOT "
                                  "NULL AFTER `room_id`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter tenant table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`tenant` CHANGE COLUMN `tenant_balance` `tenant_balance` "
                                  "INT NULL DEFAULT 0 ;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter tenant table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`tenant` ADD COLUMN `deleted` VARCHAR(45) NOT NULL "
                                  "DEFAULT 'False' AFTER `room_id`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # ================================================ payment table ===============================================

        # Creating payment table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`payment` (`payment_id` INT NOT NULL "
                                  "AUTO_INCREMENT, "
                                  "`payment_amount` INT NOT NULL, `room_id` INT NOT NULL, `tenant_id` INT NOT NULL, "
                                  "`admin_id` INT NOT NULL, `basic_user_id` INT NULL, `date_created` VARCHAR(45) NOT "
                                  "NULL, PRIMARY KEY (`payment_id`), UNIQUE INDEX `payment_id_UNIQUE` (`payment_id` "
                                  "ASC) VISIBLE);")
            print("'payment' table is created successfully")
        except Exception as e:
            print("'payment' table could not be created")
            print(e)

        # Add discount_code column to the payment table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`payment` ADD COLUMN `discount_code` VARCHAR(45) NULL "
                                  "AFTER `date_created`;")
            print("discount_code column is added to the payment table successfully")
        except Exception as e:
            print("discount_code column could not be created successfully")
            print(e)

        # Change default to the payment table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`payment` CHANGE COLUMN `discount_code` `discount_code` "
                                  "VARCHAR(45) NULL DEFAULT NULL ;")
            print("Default is changed to the payment table successfully")
        except Exception as e:
            print("Default could not be changed successfully")
            print(e)

        # Add payment_description column to the payment table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`payment` ADD COLUMN `payment_description` VARCHAR(45) "
                                  "NOT NULL AFTER `discount_code`;")
            print("payment_description column is added to the payment table successfully")
        except Exception as e:
            print("payment_description column could not be created successfully")
            print(e)

        # Alter payment table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`payment` ADD COLUMN `time_created` VARCHAR(45) NOT NULL "
                                  "AFTER `date_created`, CHANGE COLUMN `date_created` `date_created` VARCHAR(45) NOT "
                                  "NULL AFTER `payment_description`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # ================================================ discount table ==============================================

        # Creating discount table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`discount` ( `discount_id` INT NOT NULL "
                                  "AUTO_INCREMENT, "
                                  "`discount_code` VARCHAR(45) NOT NULL, `discount_amount` INT NOT NULL, `admin_id` "
                                  "INT NOT NULL, `basic_user_id` INT NULL, `date_created` VARCHAR(45) NOT NULL, "
                                  "PRIMARY KEY (`discount_id`), UNIQUE INDEX `discount_code_UNIQUE` "
                                  "(`discount_code` ASC) VISIBLE, UNIQUE INDEX `discount_id_UNIQUE` "
                                  "(`discount_id` ASC) VISIBLE);")
            print("'discount' table is created successfully")
        except Exception as e:
            print("'discount' table could not be created")
            print(e)

        # Add discount_status column to the discount table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`discount` ADD COLUMN `discount_status` VARCHAR(45) NOT "
                                  "NULL AFTER `date_created`;")
            print("discount_status column is added to the room table successfully")
        except Exception as e:
            print("discount_status column could not be created successfully")
            print(e)

        # Alter discount table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`discount` ADD COLUMN `time_created` VARCHAR(45) NOT NULL "
                                  "AFTER `date_created`, CHANGE COLUMN `discount_status` `discount_status` VARCHAR(45) "
                                  "NOT NULL AFTER `basic_user_id`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter discount table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`discount` ADD COLUMN `deleted` VARCHAR(45) NOT NULL "
                                  "DEFAULT 'False' AFTER `time_created`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # ================================================ action_history table ========================================

        # Creating action_history table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`action_history` (`action_id` INT "
                                  "NOT NULL, "
                                  "`action_description` VARCHAR(45) NOT NULL, `admin_id` INT NOT NULL, `current_user` "
                                  "VARCHAR(45) NOT NULL, `privilege_access` VARCHAR(45) NOT NULL, `date_created` "
                                  "VARCHAR(45) NOT NULL, PRIMARY KEY (`action_id`));")
            print("'action_history' table is created successfully")
        except Exception as e:
            print("'action_history' table could not be created")
            print(e)

        # Alter action_history table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`action_history` CHANGE COLUMN `action_id` `action_id` "
                                  "INT NOT NULL AUTO_INCREMENT ;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter action_history table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`action_history` CHANGE COLUMN `current_user` "
                                  "`user_current` VARCHAR(45) NOT NULL ;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter action_history table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`action_history` ADD COLUMN `basic_user_id` INT NULL "
                                  "DEFAULT 0 AFTER `admin_id`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter action_history table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`action_history` ADD COLUMN `time_created` VARCHAR(45) "
                                  "NOT NULL AFTER `date_created`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # ================================================ booking table ===============================================
        # Creating booking table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`booking` (`booking_id` INT NOT NULL "
                                  "AUTO_INCREMENT, "
                                  "`tenant_name` VARCHAR(45) NOT NULL, `tenant_email` VARCHAR(45) NOT NULL, `admin_id` "
                                  "INT NOT NULL, `date_created` VARCHAR(45) NOT NULL, PRIMARY KEY (`booking_id`));")
            print("'booking' table is created successfully")
        except Exception as e:
            print("'booking' table could not be created")
            print(e)

        # Alter booking table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`booking` ADD COLUMN `status` VARCHAR(45) NOT NULL AFTER "
                                  "`date_created`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter booking table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`booking` ADD COLUMN `time_created` VARCHAR(45) NOT "
                                  "NULL AFTER `date_created`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter booking table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`booking` CHANGE COLUMN `status` `booking_status` "
                                  "VARCHAR(45) NOT NULL , ADD UNIQUE INDEX `tenant_name_UNIQUE` (`tenant_name` ASC) "
                                  "VISIBLE, ADD UNIQUE INDEX `tenant_email_UNIQUE` (`tenant_email` ASC) VISIBLE;;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter booking table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`booking` ADD COLUMN `room_type` VARCHAR(45) NOT NULL "
                                  "AFTER `booking_status`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter booking table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`booking` DROP COLUMN `status`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # ================================================ notif table =================================================

        # Creating notif table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`notif` (`notif_id` INT NOT NULL "
                                  "AUTO_INCREMENT, "
                                  "`notif_subject` VARCHAR(45) NOT NULL, `notif_description` VARCHAR(45) NOT NULL, "
                                  "`date_created` VARCHAR(45) NOT NULL, `admin_id` VARCHAR(45) NOT NULL, PRIMARY KEY "
                                  "(`notif_id`));")
            print("'notif' table is created successfully")
        except Exception as e:
            print("'notif' table could not be created")
            print(e)

        # Alter notif table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`notif` ADD COLUMN `time_created` VARCHAR(45) NOT NULL "
                                  "AFTER `date_created`, CHANGE COLUMN `admin_id` `admin_id` VARCHAR(45) NOT NULL "
                                  "AFTER `notif_description`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # Alter notif table
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("ALTER TABLE `hmsdatabase`.`notif` ADD COLUMN `deleted` VARCHAR(45) NOT NULL DEFAULT "
                                  "'False' AFTER `time_created`;")
            print("alteration is added successfully")
        except Exception as e:
            print("alteration failed")
            print(e)

        # ================================================ assessment table ============================================

        # Creating assessment table in database
        try:
            self.mycursor = self.db1.cursor()
            self.mycursor.execute("CREATE TABLE IF NOT EXISTS `hmsdatabase`.`assessment` (`assessment_id` INT NOT NULL "
                                  "AUTO_INCREMENT, `assessment_amount` INT NOT NULL, `room_id` INT NULL, `tenant_id` "
                                  "INT NOT NULL, `admin_id` INT NOT NULL, `basic_user_id` INT NULL, "
                                  "`assessment_description` VARCHAR(45) NOT NULL, `date_created` VARCHAR(45) NOT NULL, "
                                  "`time_created` VARCHAR(45) NOT NULL, PRIMARY KEY (`assessment_id`));")
            print("'assessment' table is created successfully")
        except Exception as e:
            print("'notif' table could not be created")
            print(e)
