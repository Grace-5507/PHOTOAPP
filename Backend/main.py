from flask import Flask
from flask_restx import Api #Flask_restx provides a coherent collection of decorators and tools to describe  API and expose its documentation properly (using Swagger).
from auth import auth_ns
from photos import photos_ns
from users import users_ns
from album import albums_ns
from flask_jwt_extended import JWTManager
from config import DevConfig
from exts import db
from flask_migrate import Migrate
from models import Users, Albums, Photos
from flask_cors import CORS


def create_app(config):
    app=Flask(__name__)
    app.config.from_object(DevConfig)
    CORS(app) #configuring api to work with the client application
    db.init_app(app)
    migrate = Migrate(app, db)

    api=Api(app, doc="/docs")
    JWTManager(app)

    api.add_namespace(users_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(photos_ns)
    api.add_namespace(albums_ns)



    #exposes thus allowing us to interact with the database object via terminal shell
    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'users': Users,
            'Albums': Albums,
            'Photos': Photos
            
            }
    return app


       
