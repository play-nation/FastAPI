from fastapi import FastAPI, Depends, Query
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI()

# MongoDB URI and Database name
Mongo_URI = "mongodb://localhost:27017"
DATABASE_NAME = "BankInfo"


# Dependences to get the database client
def get_database():
    client = AsyncIOMotorClient(Mongo_URI)
    db = client[DATABASE_NAME]
    return db

# Pydentic model for the document
class Item(BaseModel):
    name:str
    address:str
    phone: int


# Create a route to interact with Mongodb
@app.post("/items/")
async def create_item(item: Item, db=Depends(get_database)):
    collection = db['items']
    result =  await collection.insert_one(item.dict())
    return {"id": str(result.inserted_id)}

@app.get("/items/", response_model = List[Item])
async def get_items(
    name: Optional[str] = Query(None, description="Filter items by name"),
    address: Optional[str] = Query(None, description="Filter items by address"),
    phone: Optional[int] = Query(None, description="Filter items by phone"),   
    db = Depends(get_database)):
    
    collection = db["items"]

    query={}

    if name:
        query["name"]=name
    if address:
        query["address"]=address
    if phone:
        query["phone"]=phone


    items_cursor = collection.find(query)
    items = []

    async for item in items_cursor:
        items.append(Item(**item))

    if not items:
        return {"message": "No items found."}
    
    return items    


