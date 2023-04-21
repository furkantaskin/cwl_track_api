from fastapi import FastAPI
from typing import Dict, List

app = FastAPI()

service_dict = Dict[str, int | bool]
services_list = List[service_dict]


service_list: Dict[str, services_list] = {
    "services": [
        {
            "name": "crater",
            "url": "https://crater.com.tr",
            "type": "domain",
            "startedAt": "2021-01-01",
            "finishAt": "2024-01-01",
            "price": 1000,
            "paid": "False",
            "currency": "TRY",
            "customer": "Özal Acar"
        },
        {
            "name": "basovali",
            "url": "https://basovali.com",
            "type": "hosting",
            "startAt": "2021-01-01",
            "finishAt": "2023-01-01",
            "price": 300,
            "paid": True,
            "currency": "EUR",
            "customer": "Emin Göroğlu"
        }
    ]
}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/services")
async def get_services():
    return service_list


