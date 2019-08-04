from aiohttp import web


async def handle_test(request):
    return web.Response(text='ok')



