from pydantic import BaseModel

class connectionString:
    def  __init__(self , host , userName , passWord) -> None:
        self.host =host
        self.user = userName
        self.password = passWord


class Product:
    def __init__(self, product_id, name,sku,wherehouseId, price  , qty , catID):
        self.id = product_id
        self.ProductName = name
        self.ProductSKU = sku
        self.WereHouseID = wherehouseId
        self.Price = price
        self.Quantity = qty
        self.CategoryID  = catID


class ProductModel(BaseModel):
    
    id : int
    ProductName :str
    ProductSKU: str
    WereHouseID :int
    Price :float
    Quantity : int
    CategoryID : int 