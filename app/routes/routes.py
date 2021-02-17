from app import api
from ..views.users import Usuarios
from ..views.listemUsers import ListemUsers



# EndPoint para acesso ás opções de Usuários
api.add_resource(Usuarios, '/user')

# Endpoint para retorno de todos os usuários
api.add_resource(ListemUsers, '/users')

