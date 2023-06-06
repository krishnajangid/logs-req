import asyncio

import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from controllers.log import LogBuffer
from models.models import init_db
from utils.common import get_logger
from utils.config import settings
from views import router

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

LOGGER = get_logger()


@app.exception_handler(Exception)
async def exception_error_handler(request: Request, exc: Exception):
    LOGGER.error(f"Error while process data. Error: {exc}.")
    return JSONResponse(
        status_code=500,
        content={"message": "Something went wrong. Please try agan later."},
    )


@app.on_event("startup")
async def startup_event():
    init_db()
    log_buffer = LogBuffer()
    asyncio.create_task(log_buffer.flush_logs_periodically())


if __name__ == "__main__":
    uvicorn.run(
        "run:app",
        host=settings.HTTP_HOST,
        port=settings.HTTP_PORT,
        reload=settings.DEBUG_MODE
    )
