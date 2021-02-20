from flask import Response
from flask_restful import Resource
from bson import json_util
from ..models.mongodb import mongo_get_all_users



class ListemUsers(Resource):
    def get(self):
        user = mongo_get_all_users()
        response = json_util.dumps(user)
        return Response(response, mimetype='application/json')