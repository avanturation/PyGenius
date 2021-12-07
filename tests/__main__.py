import asyncio
from pygenius import GeniusClient

CLIENT_ID = "topsecret"
CLIENT_SECRET = "topsecret"


async def fetch_keung():
    client = GeniusClient(CLIENT_ID, CLIENT_SECRET)
    result = await client.search(q="새꺄, 유명하다 왜?")

    print(result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_keung())
