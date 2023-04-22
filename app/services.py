from app.types import ServiceList
import json


def read_services() -> ServiceList:
    with open("res/services.json", "r") as f:
        service_list = json.load(f)
    return service_list

