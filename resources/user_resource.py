from flask import request, jsonify, abort
from flask_restful import Resource
from models.user import User
from persistence.data_manager import DataManager

data_manager = DataManager()

class UserResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')

        # Validation
        if not email or not password:
            return {"message": "Email and password are required"}, 400
        if not isinstance(email, str) or not isinstance(password, str) or not isinstance(first_name, str) or not isinstance(last_name, str):
            return {"message": "Invalid input types"}, 400

        existing_users = data_manager.list('User')
        if any(user['email'] == email for user in existing_users):
            return {"message": "Email already exists"}, 409

        try:
            user = User(email=email, password=password, first_name=first_name, last_name=last_name)
            data_manager.save(user)
            return user.to_dict(), 201
        except ValueError as e:
            return {"message": str(e)}, 409

    def get(self, user_id=None):
        if user_id:
            user = data_manager.get(user_id, 'User')
            if user:
                return jsonify(user), 200
            return {"message": "User not found"}, 404
        else:
            users = data_manager.list('User')
            return jsonify(users), 200

    def put(self, user_id):
        user_data = data_manager.get(user_id, 'User')
        if not user_data:
            return {"message": "User not found"}, 404

        data = request.get_json()
        if 'email' in data:
            if not isinstance(data['email'], str):
                return {"message": "Invalid email type"}, 400
            user_data['email'] = data['email']
        if 'first_name' in data:
            if not isinstance(data['first_name'], str):
                return {"message": "Invalid first name type"}, 400
            user_data['first_name'] = data['first_name']
        if 'last_name' in data:
            if not isinstance(data['last_name'], str):
                return {"message": "Invalid last name type"}, 400
            user_data['last_name'] = data['last_name']

        user = User(**user_data)
        data_manager.update(user)
        return jsonify(user.to_dict()), 200

    def delete(self, user_id):
        user_data = data_manager.get(user_id, 'User')
        if not user_data:
            return {"message": "User not found"}, 404
        data_manager.delete(user_id, 'User')
        return '', 204
