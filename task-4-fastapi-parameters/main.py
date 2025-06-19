from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#: Path Parameters
@app.get("/product/{product_api}")
def get_product_by_api(product_id:int):
    return{"message": f"Product with ID {product_id} fetched successfully"}


# : Query Parameters
@app.get("/search/")
def search_products(keyword:str = "" , limit: int = 10):
    return {"keyword" : keyword , "limit" : limit}



# Request Body (Using Pydantic)
class Product(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/add-product/")
def add_product(product:Product):
    return {"message" : "Product added!" , "product" : product}


