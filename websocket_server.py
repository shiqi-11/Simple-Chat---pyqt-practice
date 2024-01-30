import asyncio
import websockets
from ratel_imiter import checkLimit

async def echo(websocket, path):
    async for message in websocket:
        if checkLimit():
            await websocket.send(message)
        else:
            await  websocket.send("Too many requests, please try later!")


def start_server():
    server = websockets.serve(echo, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    start_server()
