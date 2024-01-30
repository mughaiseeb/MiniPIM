# make queries for the PIM (product operator : select - update - create - delete , Categories operator : select - update - create - delete)
# 
import ConnectionStringInit
import DB_Ops 
from Models import Product


databaseName = "pimdb"
connn = ConnectionStringInit.GetConText()
db= DB_Ops.DB_Info(
   host=connn.host,
        user=connn.user,         
        password=connn.password,
       database=databaseName

)

def getProducts():
    db.connect()
    db.use_database()
    query  = "SELECT * FROM products"
    productsRowa = db.execute_select_query(query)
    db.disconnect()
    products = []
    if productsRowa:
        for row in productsRowa:
            product = Product(row[0] , row[1] ,row[2],row[3],row[4],row[5],row[6] )
            products.append(product)
            
        return products
    else:
        return []


def getProductById(id):
    db.connect()
    db.use_database()
    query  = f"SELECT * FROM products WHERE id ={id} "
    productsRowa = db.execute_select_query(query)
    db.disconnect()
    products = []
    if productsRowa:
        for row in productsRowa:
            product = Product(row[0] , row[1] ,row[2],row[3],row[4],row[5],row[6] )
            products.append(product)
            
        return products
    else:
        return []

def getProductBySKU(sku):
    db.connect()
    db.use_database()
    query  = f"SELECT * FROM products WHERE ProductSKU ='{sku}' "
    productsRowa = db.execute_select_query(query)
    db.disconnect()
    products = []
    if productsRowa:
        for row in productsRowa:
            product = Product(row[0] , row[1] ,row[2],row[3],row[4],row[5],row[6] )
            products.append(product)
            
        return products
    else:
        return []



def createNewProduct(product: Product):
    db.connect()
    db.use_database()

    query = f"INSERT INTO products (ProductName, ProductSKU, WereHouseID, Price, Quantity , CategoryID) VALUES ('{product.ProductName}', '{product.ProductSKU}', {product.WereHouseID}, {product.Price}, {product.Quantity} , {product.CategoryID})"
    #  I'll update to query buliding function instad of here 
    productIdResult = db.exeute_insert_query(query)
    db.disconnect()
    return productIdResult # return inserted Product Id

def updateProduct(product: Product): # add check for the product id if exists
    db.connect()
    db.use_database()
    values  = buildProductUpdateQuery(product)
    query = f"UPDATE products SET {values} WHERE id = {product.id}"
    # print ("update query is : " +query) # testing
    productIdResult = db.execute_delete_update_query(query)
    db.disconnect()
    return productIdResult # return inserted Product Id

def deleteProduct(productId):
    
    db.connect()
    db.use_database()
    query  = f"DELETE FROM products WHERE id = {productId}"

    # print (query)
    result = db.execute_delete_update_query(query)
    db.disconnect()
    return result

def buildProductUpdateQuery(product: Product):
    result_string = ""
    typeString = type(result_string)
    for attr_name, attr_value in product.__dict__.items():
        if attr_value is not None and attr_value != "":
            if attr_name.lower() == 'id':
                continue
            if type(attr_value)== typeString:
                result_string += f" {attr_name} = '{attr_value}',"
            else:
                result_string += f" {attr_name} = {attr_value},"
   
    return result_string [:-1]