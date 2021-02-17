from functools import update_wrapper
from flask import Flask, request, jsonify, Response
from flask_restful import Resource
from bson import json_util
from werkzeug.security import generate_password_hash
from ..models.mongodb import mongo_created_user, mongo_get_user, mongo_update_user
from .error import error
from .response import response




class Usuarios(Resource):
    def get(self):
        id = request.json['id']
        try:
            user = mongo_get_user(id)
            response = json_util.dumps(user)
            return Response(response, mimetype='application/json')
        except:
            return error()


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
            return error()


    def put(self):
        id = request.json['id']
        username = request.json['username']
        password = request.json['password']
        name = request.json['name']
        email = request.json['email']
        cellphone = request.json['cellphone']
        hashed_password = generate_password_hash(password)
        
        try:
            mongo_update_user(id, username, hashed_password, name, email, cellphone)
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
            return error()





