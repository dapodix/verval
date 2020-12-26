from verval.sso import SsoDataKemdikbud
from .base import BaseVervalSp
from .config import LOGIN_URL


class AuthVervalSP(BaseVervalSp):
    @property
    def url_log_in(self) -> str:
        res = self.session.get(LOGIN_URL, allow_redirects=False)
        return res.url

    def login(self, username: str, password: str) -> bool:
        url = self.url_log_in
        appKey = url.split("=")[-1]
        return SsoDataKemdikbud.login(appKey, username, password, self.session)
