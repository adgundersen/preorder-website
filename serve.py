from aiohttp import web

routes = web.RouteTableDef()

routes.static('/', path='./public')

@routes.get("/login")
async def hello(request):
    return web.Response(text="Hello, world")

app = web.Application()
web.run_app(app)
