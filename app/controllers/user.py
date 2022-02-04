from flask import jsonify
from flask_restful import Resource


class User(Resource):
    def get(self, id):
        data = {'name': 'nabin khadka'}
        return jsonify(data)

    def put(self, id):
        pass

    def patch(self, id):
        pass

    def delete(self, id):
        pass


class UserList(Resource):

    def get(self):
        data = [{'name': 'nabin khadka', 'email': 'sourav@gmail.com'}]
        return jsonify(data)

    def post(self):
        pass
