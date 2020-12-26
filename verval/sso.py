from bs4 import BeautifulSoup
from dataclasses import dataclass
from logging import getLogger, Logger
from requests import Session
from urllib.parse import unquote


class BaseSso(object):
    logger: Logger = getLogger("SSO-Data-Kemdikbud")
    url: str = "https://sso.data.kemdikbud.go.id/sys/login"


@dataclass
class SsoDataKemdikbud(BaseSso):
    appKey: str
    username: str
    password: str
    session: Session
    success: bool = False

    def __post_init__(self) -> None:
        self.login(self.appKey, self.username, self.password, self.session)

    @classmethod
    def login(cls, appKey: str, username: str, password: str, session: Session) -> bool:
        auth_url = cls.get_auth_url(appKey, username, password, session)
        if auth_url:
            res = session.get(auth_url)
            if res.ok:
                cls.logger.debug(f"[{username}] Berhasil login SSO!")
            else:
                cls.logger.warn(f"[{username}] Gagal login SSO!")
            return res.ok
        cls.logger.warn(f"[{username}] Gagal login SSO!")
        return False

    @classmethod
    def get_auth_url(
        cls, appKey: str, username: str, password: str, session: Session
    ) -> str:
        params = {"appKey": appKey}
        res = session.get(cls.url, params=params)
        if not res.ok:
            return ""
        cls.logger.debug(f'[{username}] Berhasil mendapatkan halaman login.')
        soup = BeautifulSoup(res.text, "html.parser")
        data = {
            "RadScriptManager1": "loginBasePanel|LoginButton",
            "RadStyleSheetManager1_TSSM": soup.find(
                "input", id="RadStyleSheetManager1_TSSM"
            )["value"],
            "RadScriptManager1_TSM": soup.find("input", id="RadScriptManager1_TSM")[
                "value"
            ],
            "__EVENTTARGET": soup.find("input", id="__EVENTTARGET")["value"],
            "__EVENTARGUMENT": soup.find("input", id="__EVENTARGUMENT")["value"],
            "__VIEWSTATE": soup.find("input", id="__VIEWSTATE")["value"],
            "__VIEWSTATEGENERATOR": soup.find("input", id="__VIEWSTATEGENERATOR")[
                "value"
            ],
            "__EVENTVALIDATION": soup.find("input", id="__EVENTVALIDATION")["value"],
            "Decorator1_ClientState": soup.find("input", id="Decorator1_ClientState")[
                "value"
            ],
            "fAppID": soup.find("input", id="fAppID")["value"],
            "inpUsername": username,
            "inpPassword": password,
            "RadCaptcha1$InvisibleTextBox": soup.find(
                "input", id="RadCaptcha1$InvisibleTextBox"
            )["value"],
            "RadCaptcha1_ClientState": soup.find("input", id="RadCaptcha1_ClientState")[
                "value"
            ],
            "LoginButton_ClientState": soup.find("input", id="LoginButton_ClientState")[
                "value"
            ],
            "__ASYNCPOST": soup.find("input", id="__ASYNCPOST")["value"],
            "RadAJAXControlID": soup.find("input", id="RadAJAXControlID")["value"],
        }
        res = session.post(cls.url, data, params=params)
        cls.logger.debug(f"[{username}] Berhasil mendapatkan url auth")
        return unquote(res.text.split("|")[7])
