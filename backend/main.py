from fastapi import FastAPI
from modules.inventory.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origin = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
