class HTTPException(Exception):
    """
    Exception which happens when HTTP status code is not 200 (OK).
    """

    def __init__(self, code, url) -> None:
        self.error = f"While requesting to {url}, request returned status {code}."

    def __str__(self) -> str:
        return self.error


class GeniusException(Exception):
    """
    Exception which happens when Genius API metadata status is not 200 (OK).
    """

    def __init__(self, code, url, msg) -> None:
        self.error = f"While requesting to {url}, Genius API returned status {code}. Genius's message: {msg}"

    def __str__(self) -> str:
        return self.error
