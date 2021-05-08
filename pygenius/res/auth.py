from typing import List, Optional
from ..utils.request import AsyncRequest


class Authentication:
    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.HTTP = AsyncRequest(client_id, client_secret)

    async def issue_token(self, scopes: Optional[List]):
        return await self.HTTP.auth(scopes)

    async def access_endpoint(self, scopes: Optional[List], endpoint, **kwargs):
        access_token = await self.issue_token(scopes)

        return await self.HTTP.request(endpoint, access_token, **kwargs)
