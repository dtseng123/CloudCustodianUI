"""The app module, containing the app factory function."""
import os
from flask import Flask, render_template, jsonify
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
    register_extensions(app)
 
    return app

 
def register_extensions(app):
    """Register Flask extensions."""
 
    db.init_app(app)
    with app.app_context():
        db.create_all()
    ma.init_app(app)
    migrate.init_app(app, db)

    return None


 