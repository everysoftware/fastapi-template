from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic_settings import BaseSettings, SettingsConfigDict


class BackendBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class BackendSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="allow")


class BackendErrorResponse(BackendBase):
    msg: str
    code: str


class BackendOK(BackendErrorResponse):
    msg: str = "Success"
    code: str = "ok"


backend_ok = BackendOK()
