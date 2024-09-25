from abc import ABC

from fastapi import BackgroundTasks

from app.cache.adapter import CacheAdapter
from app.cache.dependencies import CacheDep
from app.db.dependencies import UOWDep
from app.db.uow import UOW
from app.mail.client import MailClient
from app.mail.dependencies import MailDep


class Service(ABC):
    uow: UOW
    cache: CacheAdapter
    mail: MailClient
    background: BackgroundTasks

    def __init__(
        self,
        uow: UOWDep,
        cache: CacheDep,
        mail: MailDep,
        background: BackgroundTasks,
    ):
        self.uow = uow
        self.cache = cache
        self.mail = mail
        self.background = background
