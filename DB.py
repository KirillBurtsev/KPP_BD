import pymysql
from config import *

class DB:
    def __init__(self):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print('successfully connected')

        with self.connection.cursor() as cursor:
            create_table_query_1 = "CREATE TABLE IF NOT EXISTS Position (" \
                                   "ID_Position int NOT NULL AUTO_INCREMENT," \
                                   "Position_name varchar(20) NULL," \
                                   "PRIMARY KEY(ID_Position));"

            create_table_query_2 = "CREATE TABLE IF NOT EXISTS Work_graphic (" \
                                   "ID_Work_graphic int NOT NULL AUTO_INCREMENT," \
                                   "Work_day_start datetime NULL," \
                                   "Work_day_end datetime NULL," \
                                   "PRIMARY KEY(ID_Work_graphic));"

            create_table_query_3 = "CREATE TABLE IF NOT EXISTS Employee (" \
                                   "ID_Employee int NOT NULL AUTO_INCREMENT," \
                                   "Firstname varchar(20) NULL," \
                                   "Lastname varchar(20) NULL," \
                                   "Family_name varchar(20) NULL," \
                                   "Date_birth datetime NULL," \
                                   "ID_Position int NULL," \
                                   "ID_Work_graphic int NULL," \
                                   "FOREIGN KEY (ID_Position)  REFERENCES Position (ID_Position)," \
                                   "FOREIGN KEY (ID_Work_graphic)  REFERENCES Work_graphic (ID_Work_graphic)," \
                                   "PRIMARY KEY(ID_Employee));"

            create_table_query_4 = "CREATE TABLE IF NOT EXISTS Note (" \
                                   "ID_Note int NOT NULL AUTO_INCREMENT," \
                                   "Note_reason varchar(250) NULL," \
                                   "Note_status varchar(20) NULL," \
                                   "Time_made datetime NULL," \
                                   "PRIMARY KEY(ID_Note));"

            create_table_query_5 = "CREATE TABLE IF NOT EXISTS Employee_Note (" \
                                   "ID_Employee_Note int NOT NULL AUTO_INCREMENT," \
                                   "ID_Employee int NULL," \
                                   "ID_Note int NOT NULL," \
                                   "FOREIGN KEY (ID_Employee)  REFERENCES Employee (ID_Employee)," \
                                   "FOREIGN KEY (ID_Note)  REFERENCES Note (ID_Note)," \
                                   "PRIMARY KEY(ID_Employee_Note));"

            create_table_query_6 = "CREATE TABLE IF NOT EXISTS Penalty_reason (" \
                                   "ID_Penalty_reason int NOT NULL AUTO_INCREMENT," \
                                   "Reason_name varchar(250) NULL," \
                                   "PRIMARY KEY(ID_Penalty_reason));"

            create_table_query_7 = "CREATE TABLE IF NOT EXISTS Penalty (" \
                                   "ID_Penalty int NOT NULL AUTO_INCREMENT," \
                                   "Payment_status varchar(20) NULL," \
                                   "Penalty_date datetime NULL," \
                                   "ID_Penalty_reason int NULL," \
                                   "FOREIGN KEY (ID_Penalty_reason)  REFERENCES Penalty_reason (ID_Penalty_reason)," \
                                   "PRIMARY KEY(ID_Penalty));"

            create_table_query_8 = "CREATE TABLE IF NOT EXISTS Employee_Penalty (" \
                                   "ID_Employee_Penalty int NOT NULL AUTO_INCREMENT," \
                                   "ID_Employee int NULL," \
                                   "ID_Penalty int NULL," \
                                   "FOREIGN KEY (ID_Employee)  REFERENCES Employee (ID_Employee)," \
                                   "FOREIGN KEY (ID_Penalty)  REFERENCES Penalty (ID_Penalty)," \
                                   "PRIMARY KEY(ID_Employee_Penalty));"

            create_table_query_9 = "CREATE TABLE IF NOT EXISTS Penalty_tariff (" \
                                   "ID_Penalty_tariff int NOT NULL AUTO_INCREMENT," \
                                   "Sum float NULL," \
                                   "ID_Penalty_reason int NULL," \
                                   "FOREIGN KEY (ID_Penalty_reason)  REFERENCES Penalty_reason (ID_Penalty_reason)," \
                                   "PRIMARY KEY(ID_Penalty_tariff));"

            create_table_query_10 = "CREATE TABLE IF NOT EXISTS KPP (" \
                                   "ID_KPP int NOT NULL AUTO_INCREMENT," \
                                   "Time_in datetime NULL," \
                                   "Time_out datetime NULL," \
                                   "ID_Employee int NULL," \
                                   "FOREIGN KEY (ID_Employee)  REFERENCES Employee (ID_Employee)," \
                                   "PRIMARY KEY(ID_KPP));"
            cursor.execute(create_table_query_1)
            print('Table1 created')
            cursor.execute(create_table_query_2)
            print('Table2 created')
            cursor.execute(create_table_query_3)
            print('Table3 created')
            cursor.execute(create_table_query_4)
            print('Table4 created')
            cursor.execute(create_table_query_5)
            print('Table5 created')
            cursor.execute(create_table_query_6)
            print('Table6 created')
            cursor.execute(create_table_query_7)
            print('Table7 created')
            cursor.execute(create_table_query_8)
            print('Table8 created')
            cursor.execute(create_table_query_9)
            print('Table9 created')
            cursor.execute(create_table_query_10)
            print('Table10 created')
            print('Tables has been successfully created!', end="\n\n")

        # Insert user--------
    def insert_user(self, Firstname, Lastname, Family_name, Date_birth, ID_Position, ID_Work_graphic):
        insert_query_3 = "INSERT INTO Employee (Firstname, Lastname, Family_name, Date_birth, ID_Position, ID_Work_graphic) VALUES ('{}','{}','{}','{}',{},{});".format(Firstname, Lastname, Family_name, Date_birth, ID_Position, ID_Work_graphic)
        # print(query)
        cur = self.connection.cursor()
        cur.execute(insert_query_3)
        self.connection.commit()
        print("user saved to db")
    # Fetch All
    def fetch_user(self):
        query = "select * from Employee"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    # delete user
    def delete_user(self, ID_Employee):
        query = "delete from Employee where ID_Employee= {}".format(ID_Employee)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("deleted")
    # update
    def update_user(self, ID_Employee, New_Firstname, New_Lastname, New_Family_name, New_Date_birth, New_ID_Position, New_ID_Work_graphic):
        query = "update Employee set Firstname='{}',Lastname='{}', Family_name='{}', Date_birth='{}', ID_Position={}, ID_Work_graphic={} where ID_Employee={}".format(
            New_Firstname, New_Lastname, New_Family_name, New_Date_birth, New_ID_Position, New_ID_Work_graphic, ID_Employee)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("updated")

        # Insert position ---------
    def insert_position(self, Position_name):
        insert_query_3 = "INSERT INTO Position (Position_name) VALUES ('{}');".format(Position_name)
        # print(query)
        cur = self.connection.cursor()
        cur.execute(insert_query_3)
        self.connection.commit()
        print("Position saved to db")
    # Fetch All
    def fetch_position(self):
        query = "select * from Position"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    # delete position
    def delete_position(self, ID_Position):
        query = "delete from Position where ID_Position= {}".format(ID_Position)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("position was deleted")
    # update
    def update_position(self, ID_Position, Position_name):
        query = "update Position set Position_name='{}' where ID_Position={}".format(
            Position_name, ID_Position)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("updated")

        # Insert Note ---------
    def insert_note(self, Note_reason, Note_status, Time_made):
        insert_query_3 = "INSERT INTO Note (Note_reason, Note_status, Time_made) VALUES ('{}','{}','{}');".format(Note_reason, Note_status, Time_made)
        # print(query)
        cur = self.connection.cursor()
        cur.execute(insert_query_3)
        self.connection.commit()
        print("Note saved to db")
    # Fetch All
    def fetch_note(self):
        query = "select * from Note"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    # delete note
    def delete_note(self, ID_Note):
        query = "delete from Note where ID_Note= {}".format(ID_Note)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("note was deleted")
    # update
    def update_note(self, ID_Note, Note_reason, Note_status, Time_made):
        query = "update Note set Note_reason='{}',Note_status='{}',Time_made='{}' where ID_Note={}".format(Note_reason, Note_status, Time_made, ID_Note)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("updated")

        # Insert Work_graphic ---------
    def insert_work_graphic(self, Work_day_start, Work_day_end):
        insert_query_3 = "INSERT INTO Work_graphic (Work_day_start, Work_day_end) VALUES ('{}','{}');".format(
            Work_day_start, Work_day_end)
        # print(query)
        cur = self.connection.cursor()
        cur.execute(insert_query_3)
        self.connection.commit()
        print("Work graphic saved to db")
    # Fetch All
    def fetch_work_graphic(self):
        query = "select * from Work_graphic"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    # delete work_graphic
    def delete_work_graphic(self, ID_Work_graphic):
        query = "delete from Work_graphic where ID_Work_graphic= {}".format(ID_Work_graphic)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("Work graphic was deleted")
    # update
    def update_work_graphic(self, ID_Work_graphic, Work_day_start, Work_day_end):
        query = "update Work_graphic set Work_day_start='{}',Work_day_end='{}' where ID_Work_graphic={}".format(
            Work_day_start, Work_day_end, ID_Work_graphic)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("updated")

        # Insert KPP--------
    def insert_kpp(self, Time_in, Time_out, ID_Employee):
        insert_query_3 = "INSERT INTO KPP (Time_in, Time_out, ID_Employee) VALUES ('{}','{}',{});".format(Time_in, Time_out, ID_Employee)
        # print(query)
        cur = self.connection.cursor()
        cur.execute(insert_query_3)
        self.connection.commit()
        print("Kpp record saved to db")
    # Fetch All
    def fetch_kpp(self):
        query = "select * from KPP"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    # delete kpp
    def delete_kpp(self, ID_KPP):
        query = "delete from KPP where ID_KPP= {}".format(ID_KPP)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("deleted")
    # update
    def update_kpp(self, ID_KPP, New_Time_in, New_Time_out, New_ID_Employee):
        query = "update KPP set Time_in='{}',Time_out='{}',ID_Employee={} where ID_KPP={}".format(
            New_Time_in, New_Time_out, New_ID_Employee, ID_KPP)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("updated")

        # Insert Penalty--------
    def insert_penalty(self, ID_Penalty_reason, Payment_status, Penalty_date):
        insert_query_3 = "INSERT INTO Penalty (ID_Penalty_reason, Payment_status, Penalty_date) VALUES ({},'{}','{}');".format(ID_Penalty_reason, Payment_status, Penalty_date)
        # print(query)
        cur = self.connection.cursor()
        cur.execute(insert_query_3)
        self.connection.commit()
        print("Penalty record saved to db")
    # Fetch All
    def fetch_penalty(self):
        query = "select * from Penalty"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    # delete penalty
    def delete_penalty(self, ID_Penalty):
        query = "delete from Penalty where ID_Penalty= {}".format(ID_Penalty)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("deleted")
    # update
    def update_penalty(self, ID_Penalty, New_ID_Penalty_reason, New_Payment_status, New_Penalty_date):
        query = "update Penalty set ID_Penalty_reason={},Payment_status='{}',Penalty_date='{}' where ID_Penalty={}".format(
            New_ID_Penalty_reason, New_Payment_status, New_Penalty_date, ID_Penalty)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("updated")

        # Insert Penalty_reason ---------
    def insert_penalty_reason(self, Reason_name):
        insert_query_3 = "INSERT INTO Penalty_reason (Reason_name) VALUES ('{}');".format(Reason_name)
        # print(query)
        cur = self.connection.cursor()
        cur.execute(insert_query_3)
        self.connection.commit()
        print("Penalty reason saved to db")
    # Fetch All
    def fetch_penalty_reason(self):
        query = "select * from Penalty_reason"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    # delete penalty_reason
    def delete_penalty_reason(self, ID_Penalty_reason):
        query = "delete from Penalty_reason where ID_Penalty_reason= {}".format(ID_Penalty_reason)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("Penalty reason was deleted")
    # update
    def update_penalty_reason(self, ID_Penalty_reason, Reason_name):
        query = "update Penalty_reason set Reason_name='{}' where ID_Penalty_reason={}".format(
            Reason_name, ID_Penalty_reason)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("updated")

        # Insert Penalty_tariff--------
    def insert_penalty_tariff(self, ID_Penalty_reason, Sum):
        insert_query_3 = "INSERT INTO Penalty_tariff (ID_Penalty_reason, Sum) VALUES ({},{});".format(ID_Penalty_reason, Sum)
        # print(query)
        cur = self.connection.cursor()
        cur.execute(insert_query_3)
        self.connection.commit()
        print("Penalty tariff saved to db")
    # Fetch All
    def fetch_penalty_tariff(self):
        query = "select * from Penalty_tariff"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    # delete penalty
    def delete_penalty_tariff(self, ID_Penalty_tariff):
        query = "delete from Penalty_tariff where ID_Penalty_tariff= {}".format(ID_Penalty_tariff)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("deleted")
    # update
    def update_penalty_tariff(self, ID_Penalty_tariff, New_ID_Penalty_reason, Sum):
        query = "update Penalty_tariff set ID_Penalty_reason={},Sum={}, where ID_Penalty_tariff={}".format(
            New_ID_Penalty_reason, Sum, ID_Penalty_tariff)
        print(query)
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        print("updated")