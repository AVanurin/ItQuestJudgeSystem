from aiohttp import web
import handlers


def build():
    app = web.Application()
    app.add_routes([web.get('/', handlers.handle_test)])


    return app
