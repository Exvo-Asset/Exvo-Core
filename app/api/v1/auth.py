from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import datetime


router = APIRouter()


class LoginIn(BaseModel):
username: str
password: str


@router.post('/login')
def login(payload: LoginIn):
# dummy auth for skeleton
if payload.username == 'admin' and payload.password == 'password':
return {'access_token': 'fake-jwt-token', 'token_type': 'bearer', 'expires': datetime.datetime.utcnow().isoformat()}
raise HTTPException(status_code=401, detail='Invalid credentials')
