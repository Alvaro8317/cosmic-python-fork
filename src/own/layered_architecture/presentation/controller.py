from fastapi import APIRouter
from business import service

router = APIRouter()


@router.get("/messages")
async def get_messages():
    return service.service_messages()
