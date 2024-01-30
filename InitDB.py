# init database and add super user 
# read connection string from DB_ConText.text
# create the database from the file DB_Details.txt 

import DB_Ops 
import ConnectionStringInit


databaseName = "pimdb"

connn = ConnectionStringInit.GetConText()

db= DB_Ops.DB_Info(
   host=connn.host,
        user=connn.user,         
        password=connn.password,
       database=databaseName

)


db.connect()
db.create_database() # create New Database with PIMDB name
db.use_database()


#  Create Users , Products and categories tables
table_columns = "id INT AUTO_INCREMENT PRIMARY KEY, UserName VARCHAR(50), UserEmail VARCHAR(200), UserPass VARCHAR(50) , UserRoll VARCHAR(5) , UserToken VARCHAR(255) "
db.create_table("Users ",table_columns)

table_columns = "id INT AUTO_INCREMENT PRIMARY KEY, ProductName VARCHAR(100), ProductSKU VARCHAR(100) ,WereHouseID INT , Price DECIMAL(10,2) , Quantity INT , CategoryID INT"
db.create_table("Products",table_columns)

table_columns = "id INT AUTO_INCREMENT PRIMARY KEY, CategoryName VARCHAR(100)"
db.create_table("Categories",table_columns)


query = "INSERT INTO users (UserName, UserEmail, UserPass, UserRoll, UserToken) VALUES ('amdin', 'mhd.mahm@gmail', 'QWer!@34', 'admin', '')"
thereIsAdmin = db.check_if_admin_exist()
if thereIsAdmin:
    print("The Admin is already there!")
else:
    db.exeute_insert_query(query)



# table_columns = "id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT"
# db.create_table("Products",table_columns)


db.disconnect()