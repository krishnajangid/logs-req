from fastapi import APIRouter

import views.v1.api as v1_api
from utils.constants import API_V1_PREFIX

router = APIRouter()
router.include_router(v1_api.router, prefix=API_V1_PREFIX, tags=["API V1"])
