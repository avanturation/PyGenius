import asyncio
from pygenius import GeniusClient

CLIENT_ID = ""
CLIENT_SECRET = ""


async def am3_freestyle():
    async with GeniusClient(CLIENT_ID, CLIENT_SECRET) as client:
        result = await client.search(q="너무 시시, 난 비웃지, 이제 RVNG SEASON")
        print(result.hits[0])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(am3_freestyle())
