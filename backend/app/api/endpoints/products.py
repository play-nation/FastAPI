from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Depends
from typing import List
import logging

from backend.app.api.endpoints.crud import get_master_input, create_master_input
from backend.app.schemas.product_schemas import MasterInputBase
from backend.app.schemas.master_input import MasterInput
from backend.app.database.session import get_db_session

router = APIRouter()

# Read the data from master_input 
@router.get("/read_master_input/", response_model = List[MasterInputBase])
def read_master_input(
    session:Session = Depends(get_db_session),
    offset:int=0,
    limit: int =100 
    )-> list[MasterInputBase]:

    try:
        result = get_master_input(session, offset, limit)
        if not result:
            raise HTTPException(status_code=404, detail="Data not found")
        logging.info(f"Fetched data: {len(result)} records")
        return result
    
    except Exception as e:
        
        logging.error(f"Error fetching data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching the data: {str(e)}")
    



@router.post("/create_master_input/", response_model=MasterInputBase)
def create_master_input_endpoint(master_input: MasterInputBase, session: Session = Depends(get_db_session)):
    try:
        created_data=create_master_input(session, master_input)
        logging.info(f"Successfully created master input with ID: {created_data.id}")
        return created_data
    
    except Exception as e:
        
        logging.error(f"Error creating data: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error creating data: {str(e)}")    