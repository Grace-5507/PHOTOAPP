from flask_restx import Namespace, Resource, fields
from models import Albums
from flask_jwt_extended import jwt_required




albums_ns = Namespace("albums", description="A namespace for Albums")

albums_model = albums_ns.model(
    "Albums",
   {"id": fields.Integer(), "user_id": fields.String(), "album_title": fields.String},
)

@albums_ns.route("/Hello")
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello world"}

@albums_ns.route("/albums", methods = ['GET', 'POST'])
class albumsResource(Resource):
    @albums_ns.marshal_list_with(albums_model) #serializes the sql data returned into a json object
    def get(self):
        """Get all albums"""

        albums = Albums.query.all()

        return albums

    @albums_ns.marshal_with(albums_model)
    @albums_ns.expect(albums_model)
    @jwt_required()
    def post(self):
        """Create a new album"""

        data = request.get_json()

        new_album = albums(
            user_id=data.get("user_id"), album_title=data.get("album_title"))
        

        new_album.save()

        return new_album, 201

@albums_ns.route("/albums", methods=["GET", "PUT"])   
class albumsResource(Resource):
    @albums_ns.marshal_with(albums_model)
    def get(self, id):
        """Get a album by id"""
        album = Albums.query.get_or_404(id)

        return album

    @jwt_required()
    @albums_ns.marshal_with(albums_model)
    def put(self, id):
        """Update a album by id"""

        album_to_update = Albums.query.get(id)

        data = request.get_json()

        album_to_update.update(data.get("user_id"), data.get("album_title"))

        return album_to_update

    @jwt_required()
    @albums_ns.marshal_with(albums_model)
    def delete(self, id):
        """Delete a album by id"""

        album_to_delete = Albums.query.get_or_404(id)

        album_to_delete.delete()

        return album_to_delete