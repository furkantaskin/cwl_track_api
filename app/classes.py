from pydantic import BaseModel
from typing import Union, Dict


class Customer(BaseModel):
    id: int
    name: str
    surname: str
    email: str


class Service(BaseModel):
    service_id: int
    name: str
    url: str
    type: str
    start_date: str
    end_date: str
    price: Union[int, float]
    paid_status: bool
    currency: str
    customer_id: int


class ServiceList(BaseModel):
    services: Dict[str, Service]


class CustomerList(BaseModel):
    customers: Dict[str, Customer]
