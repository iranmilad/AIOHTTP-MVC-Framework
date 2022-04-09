import json
import requests
from aiohttp import web
from Controllers.Controller import Controller
# models
from Model.User import Users

class UserController(Controller):
    
    async def add_user(request):
        data = json.loads(await request.text())
        
        user = await Users.create(
            user = data['user'],
            password = data['password'],
        )
        return web.json_response({"user": user.user})



    async def get_user(request):

        data = json.loads(await request.text())
        
        userName=data['user']
        user = await Users.get(user=userName)
        
        return web.json_response({"status":"success", "user": user.user}) 
