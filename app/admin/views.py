from typing import Any

import humanize
from sqladmin import ModelView

from app.db import UserOrm
from app.db.utils import naive_utc


def time_format(m: Any, a: Any) -> Any:
    return humanize.naturaltime(getattr(m, a), when=naive_utc())


class BaseView(ModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    can_export = True

    column_sortable_list = [
        "created_at",
        "updated_at",
    ]

    column_default_sort = [("created_at", True)]

    column_formatters = {
        "created_at": time_format,
        "updated_at": time_format,
    }


class UserAdmin(BaseView, model=UserOrm):
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"

    column_list = [
        UserOrm.id,
        UserOrm.email,
        UserOrm.first_name,
        UserOrm.is_active,
        UserOrm.is_superuser,
        UserOrm.is_verified,
        UserOrm.created_at,
        UserOrm.updated_at,
    ]

    column_searchable_list = [
        UserOrm.email,
    ]
