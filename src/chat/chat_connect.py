import aiohttp
import time
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        cliend_id = int(time.time() * 1000)
        async with session.ws_connect(f'http://localhost:8000/chat/ws/{cliend_id}') as ws:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    with open("ws_message.txt", "a") as file:
                        file.write(f"{msg.data}\n")

asyncio.run(main())