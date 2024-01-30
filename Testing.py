# this file is for testing project functions 

import PIM_DB
from Models import Product
from decimal import Decimal
products = PIM_DB.getProducts()
for product in products:
    print(product.id)
    print(product.ProductName)
    print(product.ProductSKU)
    print(product.WereHouseID)
    print(product.Price)
    print(product.Quantity)
    print(product.CategoryID)

# products = PIM_DB.getProducts()
# print(products)
# -----------------------Create Product
# product = Product(5 , "Monster TNT" , None , None, 19999.99 ,None , None)

# insertedProductID = PIM_DB.createNewProduct(product)

# print(insertedProductID)

# *********************************


# ----------------update product
# price = Decimal("19999.99")
# product = Product(id = 5 , ProductName="Monster TNT pro max" , ProductSKU= "MON10005" , WereHouseID= 2, Price= 22229.99 , Quantity= 10 , CategoryID= 5)
# success = PIM_DB.updateProduct(product)
# print (success)
# test = PIM_DB.buildProductUpdateQuery(product)
# print (test)
# print(type(test))

# if type(test) == 'str':
#     print ("it is string")
# else:
#     print ("not string")


    