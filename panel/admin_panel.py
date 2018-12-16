from sanic.response import json
from sanic import Blueprint

panel = Blueprint(name='admin_panel')

@panel.route('/')
async def index(request):
    return json({'my': 'panel użytkownika - administratora'})