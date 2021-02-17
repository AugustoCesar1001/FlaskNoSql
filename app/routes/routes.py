from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api, reqparse
from bson import json_util
from app import api, mongo
from werkzeug.security import generate_password_hash
from bson.objectid import ObjectId
from ..models.mongodb import mongo_created_user


class Usuarios(Resource):
    def get(self):
        id = request.json['id']
        user = mongo.db.users.find_one({'_id' : str(id)})
        response = json_util.dumps(user)
        return Response(response, mimetype='application/json')

    def post(self):
        username = request.json['username']
        password = request.json['password']
        name = request.json['name']
        email = request.json['email']
        cellphone = request.json['cellphone']
        hashed_password = generate_password_hash(password)

        try:
            id = mongo_created_user(username, hashed_password, name, email, cellphone)
            response = {
                'id': str(id),
                'username': username,
                'password': hashed_password,
                'name': name,
                'email': email,
                'cellphone': cellphone
            }
            return response, 201
        except:
            return jsonify({'message' : 'Insucesso no Registro do Usuário', 'data': {}}), 500


class ListemUsers(Resource):
    def get(self):
        user = mongo.db.users.find()
        response = json_util.dumps(user)
        return Response(response, mimetype='application/json')




api.add_resource(Usuarios, '/user')
api.add_resource(ListemUsers, '/users')
