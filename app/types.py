from typing import List, TypedDict


class Service(TypedDict):
    name: str
    url: str
    type: str
    startAt: str
    finishAt: str
    price: float
    paid: bool
    currency: str
    customer: str


class ServiceList(TypedDict):
    services: List[Service]
