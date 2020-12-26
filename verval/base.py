from logging import getLogger
from requests import Session

from .config import REQUESTS_HEADERS


class BaseVerval(object):
    def __init__(self):
        self.logger = getLogger()
        self.session = Session()
        self.session.headers.update(REQUESTS_HEADERS)
        super().__init__()
