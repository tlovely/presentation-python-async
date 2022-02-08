from asyncio import sleep
from aiohttp import web

routes = web.RouteTableDef()

data = {
    "count": 0
}


@routes.get('/count')
async def count(request):
    await sleep(float(request.query.get("delay", 0)))
    data["count"] += 1
    return web.json_response(data["count"])


app = web.Application()
app.add_routes(routes)
