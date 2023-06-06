from utils.config import settings

API_V1_PREFIX: str = "/api/v1"
MAX_FILE_SIZE: int = 10 * 1024 * 1024
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}" \
                          f"/{settings.DB_NAME}"
