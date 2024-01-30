from fastapi import FastAPI , Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from Models import Product
from Models import ProductModel
import PIM_DB


app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "Welcome to mini PIM"}

@app.get("/products")
async def get_products():# Get all Products
    products = PIM_DB.getProducts()
    print(products)
    return {"Products": products} # return all products



@app.get("/products/{product_id}")
async def get_product_by_id(product_id: int) :
    product = PIM_DB.getProductById(product_id)
    if not product:
        raise HTTPException(
            status_code=404, detail=f"Product with id:{product_id} dose not exist"
        )
    return {product[0]} 
    # return {"product":f"{product_id}"} # return product by id

@app.post("/products")
async def post_product(product: ProductModel):
    productId = PIM_DB.createNewProduct(product)
    return {f"New Product Added with id {productId}"}

@app.delete("/products/{id}")
async def delete_product(id):
    result = PIM_DB.deleteProduct(id)
    if not result:
         raise HTTPException(
            status_code=404, detail=f"Product with id:{id} dose not exist"
        )
    return {"Prodcut Deleted"}

@app.put("/products")
async def update_product(product: ProductModel):
    
    success = PIM_DB.updateProduct(product)

    if success:
        return {f"Product with id {product.id}  updated successfully !"}
    return {f"Product with id : ({product.id}) Not found"}
# # get users
# @app.get("/users")
# async def get_users(): #get all users
#     return {"Users":"get all users"} # return all users

# # add new user
# @app.post("/users")
# async def create_user(): # create new user 
#     return 


# # update user 
# @app.get("/users/{user_id}")
# async def get_user_by_id(user_id): # get user by id 
#     return 

# # delete user
# @app.delete("/users/{usr_id}")
# async def delete_user(user_id): # delete user 
#     return


# @app.get("/categories")
# async def get_all_categories():
#     return # return all categories

# @app.get("/categories/{category_id}")
# async def get_cate_by_id(category_id):
#     return # 

