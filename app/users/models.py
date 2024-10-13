from sqlalchemy import Boolean
from sqlalchemy.orm import mapped_column, Mapped

from app.db.base import BaseOrm
from app.db.mixins import TimestampMixin, UUID4Mixin


class UserOrm(BaseOrm, UUID4Mixin, TimestampMixin):
    __tablename__ = "users"

    first_name: Mapped[str]
    last_name: Mapped[str | None]
    email: Mapped[str] = mapped_column(index=True)
    hashed_password: Mapped[str | None]
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
