import asyncio
import websockets
from ratel_imiter import checkLimit

async def echo(websocket, path):
    client_ip = websocket.remote_address[0]
    print(client_ip)

    async for message in websocket:
        isnotLimited = checkLimit(client_ip)
        print(message, isnotLimited)
        if isnotLimited:
            await websocket.send(message)
        else:
            print(f"checkLimit is {checkLimit(client_ip)}, start send error")
            await websocket.send("error")


def start_server():
    server = websockets.serve(echo, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    start_server()
