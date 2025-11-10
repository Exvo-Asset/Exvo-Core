from fastapi import FastAPI
from app.api.v1 import auth, assets, markets


app = FastAPI(title="Exvo Core Service")
app.include_router(auth.router, prefix="/v1/auth")
app.include_router(assets.router, prefix="/v1/assets")
app.include_router(markets.router, prefix="/v1/markets")


@app.get("/health")
def health():
return {"status": "ok"}
