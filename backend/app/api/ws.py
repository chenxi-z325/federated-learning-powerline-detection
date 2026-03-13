# WebSocket Real-Time Communication

import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(echo, "localhost", 6789):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())