from fastapi import FastAPI
from sqladmin import Admin

from app.admin.auth import auth_backend
from app.admin.views import UserAdmin
from app.db.connection import async_engine

app = FastAPI()
admin = Admin(
    app, async_engine, authentication_backend=auth_backend, base_url="/"
)

admin.add_view(UserAdmin)
