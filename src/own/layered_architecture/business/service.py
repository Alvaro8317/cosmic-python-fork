import random
from database import database


def validate_request():
    return random.choice([True, False])


def service_messages() -> dict:
    is_valid_request: bool = validate_request()
    if is_valid_request:
        return database.static_database
    return {"message": "Invalid request"}
