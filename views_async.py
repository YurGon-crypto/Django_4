from aiohttp import web
import asyncio

async def async_endpoint1(request):
    await asyncio.sleep(1)
    return web.Response(text="Async Endpoint 1")

async def async_endpoint2(request):

    await asyncio.sleep(2)
    return web.Response(text="Async Endpoint 2")

async def async_endpoint3(request):

    await asyncio.sleep(3)
    return web.Response(text="Async Endpoint 3")
