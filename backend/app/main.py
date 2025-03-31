from fastapi import FastAPI, Depends, APIRouter
# from backend.app.database.session import SessionDep
# from backend.app.schemas.product_schemas import Master_input
# from sqlalchemy import select
from backend.app.api.endpoints.products import router as product_router
from sqlalchemy.orm import session
from backend.app.database.session import SessionLocal
from backend.app.api.endpoints import products
import logging
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Include products router with /api prefix
# app.include_router(products.router, prefix="/api/products")


@app.get("/")
def welcome():
    return {"message" : "Welcome to the FastAPI Application"}

logging.basicConfig(level=logging.DEBUG)


app.include_router(product_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# @app.post("/test/")
# def create_test(testitem: Testitem, session:SessionDep) -> Testitem:
#     session.add(testitem)
#     session.commit()
#     session.refresh(testitem)
#     return testitem

# @app.get("/read_master_input/")
# def read_master_input(
#     session:SessionDep,
#     offset:int=0,
#     limit: int =100 )-> list[Master_input]:
#     master_input_instance=session.exec(select(Master_input).offset(offset).limit(limit)).all()
#     return master_input_instance

# @app.get("/test/{test_id}")
# def read_test_by_id(test_id:int, 
#               session:SessionDep) -> Testitem:
#     testitem_instance =session.get(Testitem, test_id)
#     if not testitem_instance:
#         raise HTTPException(status_code=404, detail="test not found")
#     return testitem_instance


# @app.delete("/test/{test_id}")
# def delete_test(test_id:int, session:SessionDep):
#     testitem_instance = session.get(Testitem, test_id)
#     if not testitem_instance:
#         raise HTTPException(status_code=404, detail="Test ID not found")
#     session.delete(testitem_instance)
#     session.commit()
#     return{"message":"Testitem deleted successfully"}


# if __name__ == "__main__":
#     SQLModel.metadata.create_all(engine)
#     # FastAPI startup code
