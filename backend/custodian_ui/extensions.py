# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""

# Flask Libraries 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
 
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
 