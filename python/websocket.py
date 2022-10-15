# https://apidocs.bithumb.com/reference/%EB%B9%97%EC%8D%B8-%EA%B1%B0%EB%9E%98%EC%86%8C-%EC%A0%95%EB%B3%B4-%EC%88%98%EC%8B%A0
import websockets
import asyncio
import json


async def bithumb_ws_client():
    uri = "wss://pubwss.bithumb.com/pub/ws"

    async with websockets.connect(uri, ping_interval=None) as websocket:
        greeting = await websocket.recv()
        print(greeting)

        subscribe_format = {
            "type": "ticker",
            "symbols": ["BTC_KRW"],
            "tickTypes": ["1H"]
        }
        subscribe_data = json.dumps(subscribe_format)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            print(data)


async def main():
    await bithumb_ws_client()

if __name__ == '__main__':
    asyncio.run(main())
