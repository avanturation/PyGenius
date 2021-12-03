from typing import Dict, Any, Literal
from .request import GeniusRequest

TEXT_FORMAT_TYPING = Literal["dom", "plain", "html"]


class GeniusClient(GeniusRequest):
    def __init__(self, client_id: str, client_secret: str) -> None:
        super().__init__(client_id, client_secret)

    def __create_params(self, locals: Dict[str, Any]) -> Dict[str, Any]:
        locals.pop("self")
        return {key: value for key, value in locals.items() if value is not None}

    async def annotations(self, id: int, text_format: TEXT_FORMAT_TYPING) -> Any:
        pass
