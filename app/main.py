import models
import note
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Notes CRUD")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(note.router, prefix="/api/notes", tags=["Notes"])

@app.get("/")
def root():
    return {"message": "FastAPI CRUD API running successfully"}
