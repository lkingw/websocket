import asyncio
import websockets

async def echo(websocket, path):
    print('Client connected')

    async for message in websocket:
        print(f'Received: {message}')
        await websocket.send(f'You sent: {message}')

    print('Client disconnected')

start_server = websockets.serve(echo, 'localhost', 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
