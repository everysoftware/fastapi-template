import datetime
import uuid

from sqlalchemy import Identity
from sqlalchemy.orm import mapped_column, Mapped

from app.db import utils


# https://docs.sqlalchemy.org/en/20/core/defaults.html
# https://docs.sqlalchemy.org/en/20/orm/declarative_config.html#abstract
# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#orm-declarative-mapped-column-type-map-pep593


class Mixin:
    pass


class IntegerIDMixin(Mixin):
    id: Mapped[int] = mapped_column(
        Identity(),
        primary_key=True,
        sort_order=-100,
    )


class UUID4Mixin(Mixin):
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        sort_order=-100,
    )


class TimestampMixin(Mixin):
    created_at: Mapped[datetime.datetime] = mapped_column(
        default=utils.naive_utc, sort_order=100
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        default=utils.naive_utc,
        onupdate=utils.naive_utc,
        sort_order=101,
    )
