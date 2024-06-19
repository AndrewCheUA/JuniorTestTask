from fastapi import APIRouter

from . import lcresponse



router = APIRouter()

router.include_router(lcresponse.router)