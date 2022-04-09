
from Controllers.UserController import UserController
from Controllers.AssetController import AssetController


class Routes():  
    def __init__(self,app):
        self.app = app    
        
    async def api_routes(self):
        # path dir of static file
        STATIC_PATH = os.path.join(os.path.dirname(__file__), "assets") 
        self.app.router.add_route('GET', '/api/name/{name}', AssetController.handle, name='home')
        self.app.router.add_route('POST', '/api/adduser', UserController.add_user, name='add_user')
        self.app.router.add_route('POST', '/api/getuser', UserController.get_user, name='getuser')
        
        # add new static route
        #self.app.router.add_static('/', STATIC_PATH, name='home')   



    
