from aiohttp import web



def build():
    app = web.Application()
    app.add_routes([web.get('/', handlers.handle_test)])


    return app
