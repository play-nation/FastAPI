from sqlalchemy.orm import Session
from backend.app.schemas.master_input import MasterInput
from backend.app.schemas.product_schemas import MasterInputBase
from backend.app.database.session import SessionLocal
from sqlalchemy import select
import logging


def create_master_input(db:Session, master_input = MasterInputBase):

    # Convert the Pydantic model to SQLAlchemy model
    session_master_input = MasterInput(**master_input.dict())   # Convert Pydantic to SQLAlchemy model
    db.add(session_master_input)
    db.commit()
    db.refresh(session_master_input)
    logging.info(f"Created new master input: {session_master_input.id}")

    return session_master_input


def get_master_input(
    db:Session,
    offset:int=0,
    limit: int =10):

    result =db.query(MasterInput).offset(offset).limit(limit).all()

    logging.info(f"Fetched {len(result)} records from master_input.")
    return result