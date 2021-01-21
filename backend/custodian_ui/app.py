"""The app module, containing the app factory function."""
import os
from flask import Flask, render_template, jsonify
from flask_cors import CORS
# from custodian_ui.api import register_api
from custodian_ui.settings import DevConfig
from custodian_ui.extensions import db, migrate, ma

def create_app(config_object=DevConfig):
    """An application factory, 
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__, 
        static_folder = "../../dist/static",
        template_folder="../../dist")
    
    app.config.from_object(config_object)
    app.strict_slashes = False
    CORS(app)
    register_extensions(app)
    # register_blueprints(app)
 
    return app

 
def register_extensions(app):
    """Register Flask extensions."""
 
    db.init_app(app)
    with app.app_context():
        db.create_all()
    ma.init_app(app)
    migrate.init_app(app, db)

    return None


# def register_blueprints(app):
#     """Register Flask blueprints."""

#     # API Endpoints
#     register_api(app)

#     return None


 