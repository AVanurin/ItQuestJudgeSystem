from aiohttp import web
from appbuilder import build


if __name__ == "__main__":
    web.run_app(build())
