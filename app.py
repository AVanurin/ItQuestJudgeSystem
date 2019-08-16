from aiohttp import web
from appbuilder import build


if __name__ == "__main__":
    app = build()
    web.run_app(app)

