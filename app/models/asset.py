from pydantic import BaseModel


class Asset(BaseModel):
symbol: str
name: str
category: str
