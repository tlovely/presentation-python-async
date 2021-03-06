"""
asyncio Stream API - mini redis
"""
import asyncio, socket

print(__doc__)

cache = {}
data = {
    "client_count": 0
}


async def handle_client(reader, writer):
    request = None
    data["client_count"] += 1
    client_id = data["client_count"]
    print(f'[client {client_id}] connected')
    while True:
        request = (await reader.readline()).decode('utf8')[:-1]
        print(f'[client {client_id}] -> {request[:50]}')
        response = 'ERROR'
        try:
            command, *rest = request.split(' ', 1)
            command = command.upper()
            if command == 'QUIT':
                break
            key, *args = rest[0].split(' ', 1)
            if command == 'GET':
                if key in cache:
                    response = f"OK {cache.get(key, '')}"
                else:
                    response = f"NONE"
            elif command == 'PUT':
                response = 'OK'
                cache[key] = args[0]
            elif command == 'DEL':
                response = 'OK'
                cache.pop(key, None)
        except Exception as e:  # generally bad to do this
            print(f'[server] {e}')
        print(f'[client {client_id}] <- {response[:50]}')
        writer.write(f'{response}\n'.encode('utf8'))
        await writer.drain()
    print(f'[client {client_id}] disconnected')
    writer.close()
    await writer.wait_closed()


async def run_server():
    server = await asyncio.start_server(handle_client, 'localhost', 1337)
    async with server:
        await server.serve_forever()


asyncio.run(run_server())