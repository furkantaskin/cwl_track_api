from app.services import read_services, read_customers
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get-services")
async def get_services():
    return read_services()


@app.get("/get-customers")
async def get_users():
    return read_customers()


