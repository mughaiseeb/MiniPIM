# All Database Operators
# Connection to database 
# Execute Queries 

import mysql.connector

class DB_Info:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor(buffered=True)
            print("Connected to MySQL server")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def create_database(self):
        try:
            print("this is the database name: "+self.database)
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            print(f"Database '{self.database}' created successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def use_database(self):
        try:
            self.cursor.execute(f"USE {self.database}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def create_table(self, table_name, columns):
        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
            print(f"Table '{table_name}' created successfully")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Disconnected from MySQL server")

    def exeute_insert_query(self , queryString): # let's test what it returns
        try:
            self.cursor.execute(queryString)
            
            # rows = self.cursor.fetchall()
            print("Data Inserted successfully") 
            # return rows
            self.cursor.execute("SELECT LAST_INSERT_ID()")
            inserted_id = self.cursor.fetchone()[0]

            self.connection.commit()
            return inserted_id
   
        except mysql.connector.Error as err:
            print(f"Insert Query Error: {err}") 
            return None
        # finally:
            # if self.connection.is_connected():
            #     self.disconnect(self)
    # def execute_insert_query(self, queryString):
    def check_if_admin_exist(self):
        try:
            self.cursor.execute(f"SELECT * FROM users WHERE username = 'amdin'")
            return self.cursor.fetchone() is not None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
    def execute_select_query(self , query):
        try:
            self.cursor.execute(query)
            listResult = self.cursor.fetchall() 
            return listResult
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        
    def execute_delete_update_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

