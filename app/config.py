from typing import Literal

from app.cache.config import CacheSettings
from app.db.config import DBSettings
from app.mail.config import MailSettings
from app.schemas import BackendSettings
from app.users.config import AuthSettings


class CORSSettings(BackendSettings):
    cors_headers: list[str] = ["*"]
    cors_methods: list[str] = ["*"]
    cors_origins: list[str] = ["*"]
    cors_origin_regex: str | None = None


class AppSettings(BackendSettings):
    app_name: str = "fastapiapp"
    app_env: Literal["dev", "prod"] = "dev"
    app_debug: bool = False

    app_display_name: str = "FastAPI App"
    app_version: str = "0.1.0"
    app_root_path: str = "/api/v1"
    app_description: str | None = None

    db: DBSettings = DBSettings()
    cors: CORSSettings = CORSSettings()
    auth: AuthSettings = AuthSettings()
    mail: MailSettings = MailSettings()
    cache: CacheSettings = CacheSettings()


settings = AppSettings()
