# PyGenius
> genius.com API wrapper for Python

## Example

```py
import asyncio
from pygenius import GeniusClient

CLIENT_ID = "your client id"
CLIENT_SECRET = "your client secret"


async def am3_freestyle():
    async with GeniusClient(CLIENT_ID, CLIENT_SECRET) as client:
        result = await client.search(q="너무 시시, 난 비웃지, 이제 RVNG SEASON")
        print(result.hits[0]) 
        # this will print results from https://genius.com/Dean-tabber-kim-ximya-3am-honjowolf-freestyle-lyrics


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(am3_freestyle())

```

## Features
* Asynchronous
* Object hooked as `SimpleNameSpace`
