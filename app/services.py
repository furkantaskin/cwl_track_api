from app.types import ServiceList
import json


def read_services() -> ServiceList:
    # Read services from json file
    with open("res/services.json", "r", encoding="utf-8") as f:
        service_list = json.load(f)
    return service_list

