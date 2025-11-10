from fastapi import APIRouter
from pydantic import BaseModel
from typing import List


router = APIRouter()


class Snapshot(BaseModel):
symbol: str
ts: str
price: float


# static sample
@router.get('/snapshot/{symbol}', response_model=Snapshot)
def snapshot(symbol: str):
return {'symbol': symbol.upper(), 'ts': '2025-11-09T00:00:00Z', 'price': 123.45}
