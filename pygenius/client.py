from typing import Dict, Any, Literal, Optional
from types import SimpleNamespace
from functools import wraps
from json import loads, dumps
from .request import GeniusRequest


def hooker(func):
    @wraps(func)
    async def real(self, *args, **kwargs):
        raw = await func(self, *args, **kwargs)
        return loads(dumps(raw), object_hook=lambda d: SimpleNamespace(**d))

    return real


class GeniusClient(GeniusRequest):
    def __init__(self, client_id: str, client_secret: str) -> None:
        super().__init__(client_id, client_secret)

    def __create_params(self, locals: Dict[str, Any]) -> Dict[str, Any]:
        locals.pop("self")
        return {
            key: value
            for key, value in locals.items()
            if value is not None and not "_" in value
        }

    @hooker
    async def annotations(
        self, _id: int, text_format: Literal["dom", "plain", "html"] = "dom"
    ) -> Any:
        params = self.__create_params(locals())
        return await self.send_request(endpoint=f"/annotations/{_id}", params=params)

    @hooker
    async def referents(
        self,
        created_by_id: Optional[int] = None,
        song_id: Optional[int] = None,
        web_page_id: Optional[int] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        text_format: Literal["dom", "plain", "html"] = "dom",
    ) -> Any:
        params = self.__create_params(locals())
        return await self.send_request(endpoint=f"/referents", params=params)

    @hooker
    async def songs(
        self, _id: int, text_format: Literal["dom", "plain", "html"] = "dom"
    ) -> Any:
        params = self.__create_params(locals())
        return await self.send_request(endpoint=f"/songs/{_id}", params=params)

    @hooker
    async def artists(
        self,
        _id: int,
        _fetch_songs: bool = False,
        sort: Optional[str] = None,
        per_page: Optional[int] = None,
        page: Optional[int] = None,
        text_format: Literal["dom", "plain", "html"] = "dom",
    ) -> Any:
        params = self.__create_params(locals())

        if _fetch_songs:
            endpoint = f"/artists/{_id}/songs"

        else:
            endpoint = f"/artists/{_id}"

        return await self.send_request(endpoint=endpoint, params=params)

    @hooker
    async def web_page(
        self,
        raw_annotatable_url: Optional[str] = None,
        canonical_url: Optional[str] = None,
        og_url: Optional[str] = None,
    ) -> Any:
        params = self.__create_params(locals())
        return await self.send_request(endpoint=f"/web_pages/lookup", params=params)

    @hooker
    async def search(self, q: str) -> Any:
        params = self.__create_params(locals())
        return await self.send_request(endpoint=f"/search", params=params)

    @hooker
    async def account(
        self,
        text_format: Literal["dom", "plain", "html"] = "dom",
    ) -> Any:
        params = self.__create_params(locals())
        return await self.send_request(endpoint=f"/account", params=params)
