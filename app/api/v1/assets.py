from fastapi import APIRouter
from typing import List
from pydantic import BaseModel


router = APIRouter()


class Asset(BaseModel):
symbol: str
name: str
category: str


_db = {
'AAPL': {'symbol':'AAPL','name':'Apple Inc.','category':'stocks'}
}


@router.get('/', response_model=List[Asset])
def list_assets():
return list(_db.values())


@router.get('/{symbol}', response_model=Asset)
def get_asset(symbol: str):
return _db.get(symbol.upper())
