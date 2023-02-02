from flask_restx import Resource, Namespace, fields,Api
from models import Users
from flask_jwt_extended import jwt_required
from flask import request


users_ns = Namespace("users", description="A namespace for Users")

#a serializer that will allow us to serialize the models and be able to use it in the frontend in json format
users_model = users_ns.model(
    "Users",
    {"id": fields.Integer(),
     "name": fields.String(),
     "username": fields.String(),
     "email": fields.String},
)



@users_ns.route("/users", methods = ['GET', 'POST'])
class UsersResource(Resource):
    @users_ns.marshal_list_with(users_model) #serializes the sql data returned into a json object
    def get(self):
        """Get all users"""

        users = Users.query.all()

        return users

    @users_ns.marshal_with(users_model)
    @users_ns.expect(users_model)
    @jwt_required()
    def post(self):
        """Create a new user"""

        data = request.get_json()

        new_user = Users(
            name=data.get("name"), username=data.get("username"), email=data.get("email")
        )

        new_user.save()

        return new_user, 201

@users_ns.route("/users", methods=["GET", "PUT", "DELETE"])   
class UsersResource(Resource):
    @users_ns.marshal_with(users_model)
    def get(self, id):
        """Get a user by id"""
        user = Users.query.get_or_404(id)

        return user

    @jwt_required()
    @users_ns.marshal_with(users_model)
    def put(self, id):
        """Update a user by id"""

        user_to_update = Users.query.get(id)

        data = request.get_json()

        user_to_update.update(data.get("name"), data.get("username"), data.get("email"))

        return user_to_update

    @jwt_required()
    @users_ns.marshal_with(users_model)
    def delete(self, id):
        """Delete a user by id"""

        user_to_delete = Users.query.get_or_404(id)

        user_to_delete.delete()

        return user_to_delete