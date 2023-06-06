from http import HTTPStatus

from fastapi import APIRouter

from controllers.log import LogBuffer
from schemas.v1.request import LogRequest
from utils.constants import MAX_FILE_SIZE

router = APIRouter()

log_buffer = LogBuffer()


@router.post("/logs", status_code=HTTPStatus.NO_CONTENT)
async def log_view(log: LogRequest):
    log_buffer.add_log(log.json())

    if log_buffer.get_file_size() >= MAX_FILE_SIZE or log_buffer.get_file_age() >= 30:
        await log_buffer.flush_logs()


@router.delete("/logs/clear-file", status_code=HTTPStatus.NO_CONTENT)
async def get_logs():
    log_buffer.clear_file()
