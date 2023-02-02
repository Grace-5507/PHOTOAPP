from flask_restx import Namespace, Resource, fields
from models import Photos
from flask_jwt_extended import jwt_required


photos_ns = Namespace("photos", description="A namespace for Photos")

photos_model = photos_ns.model(
    "Photos",
   {"id": fields.Integer(), "album_id": fields.Integer(),"photo_title": fields.String(), "image_url": fields.String},
)

@photos_ns.route("/Hello")
class HelloResource(Resource):
    def get(self):
        return {"message":"Hello world"}

@photos_ns.route("/photos", methods = ['GET', 'POST'])
class photosResource(Resource):
    @photos_ns.marshal_list_with(photos_model) #serializes the sql data returned into a json object
    def get(self):
        """Get all photos"""

        photos = Photos.query.all()

        return photos

    @photos_ns.marshal_with(photos_model)
    @photos_ns.expect(photos_model)
    @jwt_required()
    def post(self):
        """Create a new photo"""

        data = request.get_json()

        new_photo = photos(
            album_id=data.get("album_id"), photo_title=data.get("photo_title"), image_url=data.get("image_url")
        )

        new_photo.save()

        return new_photo, 201

@photos_ns.route("/photos", methods=["GET", "PUT"])   
class photosResource(Resource):
    @photos_ns.marshal_with(photos_model)
    def get(self, id):
        """Get a photo by id"""
        photo = Photos.query.get_or_404(id)

        return photo

    @jwt_required()
    @photos_ns.marshal_with(photos_model)
    def put(self, id):
        """Update a photo by id"""

        photo_to_update = photos.query.get(id)

        data = request.get_json()

        photo_to_update.update(data.get("album_id"), data.get("photo_title"), data.get("image_url"))

        return photo_to_update

    @jwt_required()
    @photos_ns.marshal_with(photos_model)
    def delete(self, id):
        """Delete a photo by id"""

        photo_to_delete = photos.query.get_or_404(id)

        photo_to_delete.delete()

        return photo_to_delete





