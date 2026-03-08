from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import router

app = FastAPI(title="Stock Insights Assistant")
app.include_router(router)