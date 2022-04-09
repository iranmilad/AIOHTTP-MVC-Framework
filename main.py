

from weakref import proxy
import toml
import os
import sys
from datetime import datetime 
from settings import load_config, PACKAGE_NAME
import math

from Routes.api import Routes
from aiohttp import web
from tortoise.contrib.aiohttp import register_tortoise





async def app_factory():
    configpath='config/config.toml'
    
    config = load_config(configpath)
    app = web.Application()
    app['config'] = config
    # include handler path
    app['assets_root_url'] = '/assets'    

  
    await Routes(app).api_routes()
    
    
    register_tortoise(
        app,
        db_url='mysql://root:@127.0.0.1:3306/stockfeeder',
        modules={"models": ["Model.User"]},
    )                 

    return app




if __name__ == '__main__':
    
    #adev runserver -p 8000
    web.run_app(app_factory())