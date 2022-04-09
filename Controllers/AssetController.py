import json
import requests
from aiohttp import web

from Controllers.Controller import Controller



class AssetController(Controller):
    async def handle(request):
        name = request.match_info.get('name', "Anonymous")
        text = "Helloooo, " + name
        return web.Response(text=text)

