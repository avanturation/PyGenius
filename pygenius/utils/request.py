from aiohttp import ClientSession
from typing import Optional

BASE_URL = "https://api.genius.com"


class AsyncRequest:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    async def auth(self, scopes: Optional[str]):
        async with ClientSession() as session:
            query = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "grant_type": "client_credentials",
                "scopes": "+".join(scopes[:]),
            }

            async with session.post(f"{BASE_URL}/oauth/token", params=query) as resp:
                print(await resp.text())
                if resp.status == 200:
                    data = await resp.json()
                    print(data)
                    return data["access_token"]

    async def request(self, endpoint, access_token, **kwargs):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "User-Agent": "CompuServe Classic/1.22",
        }

        async with ClientSession(headers=headers) as session:
            async with session.get(f"{BASE_URL}{endpoint}", params=kwargs) as resp:
                print(await resp.text())
                if resp.status == 200:
                    data = await resp.json()

                    if data["meta"]["status"] == 200:
                        print(data)
                        return data["response"]
