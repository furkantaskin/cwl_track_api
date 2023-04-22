from app.classes import ServiceList, Service, CustomerList, Customer
import json


def read_services() -> ServiceList:
    # Read services from json file
    with open("res/services.json", "r", encoding="utf-8") as f:
        service_list = json.load(f)
    return service_list["services"]


def read_customers() -> CustomerList:
    # Read customers from json file
    with open("res/services.json", "r", encoding="utf-8") as f:
        customer_list = json.load(f)
    return customer_list["customers"]

