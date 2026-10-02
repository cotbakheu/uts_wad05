from fastapi import FastAPI
from modules.inventory.routes import router

app = FastAPI()

app.include_router(router)
