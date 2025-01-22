from fastapi import FastAPI
from database import init_db
from routers import shorten, redirect, analytics

app = FastAPI()

init_db()

app.include_router(shorten.router, prefix="/api")
app.include_router(redirect.router)
app.include_router(analytics.router, prefix="/api")
