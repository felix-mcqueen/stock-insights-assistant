from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Stock Insights Assistant")
app.include_router(router)