from aiohttp import ClientSession
from typing import Optional, Any

from .exceptions import HTTPException, GeniusException

BASE_URL = "https://api.genius.com"


class Base:
    def __init__(self) -> None:
        self.session: Optional[ClientSession] = None

    async def request(
        self,
        url: str,
        method: str,
        return_type: str,
        **kwargs: Any,
    ):
        if not self.session or self.session.closed:
            self.session = ClientSession()

        resp = await self.session.request(method, url, **kwargs)

        if resp.status == 200:
            return await getattr(resp, return_type)()

        else:
            raise HTTPException(resp.status, url)

    async def post(self, url: str, **kwargs: Any):
        if not self.session or self.session.closed:
            self.session = ClientSession()

        return await self.request(url, "POST", **kwargs)

    async def get(self, url: str, **kwargs: Any):
        if not self.session or self.session.closed:
            self.session = ClientSession()

        return await self.request(url, "GET", **kwargs)


class AsyncRequest(Base):
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    async def auth(self, scopes: Optional[str]):
        query = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scopes": "+".join(scopes[:]),
        }

        resp = await self.post(
            f"{BASE_URL}/oauth/token", return_type="json", params=query
        )

        return resp["access_token"]

    async def request(self, endpoint, access_token, **kwargs):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "User-Agent": "CompuServe Classic/1.22",
        }

        resp = await self.get(
            f"{BASE_URL}{endpoint}", return_type="json", params=kwargs, headers=headers
        )

        if resp["meta"]["status"] == 200:
            return resp

        else:
            raise GeniusException(
                resp["meta"]["status"], f"{BASE_URL}{endpoint}", resp["meta"]["message"]
            )
