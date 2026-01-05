from flask import Flask
from .db import db, migrate
from flask_cors import CORS
import os
# Import models, blueprints, and anything else needed to set up the app or database
from .models.board import Board
from .routes.card_routes import cards_bp
from .routes.board_routes import boards_bp

def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    migrate.init_app(app, db)

    if config:
        app.config.update(config)

    # Initialize app with SQLAlchemy db and Migrate

    # Register Blueprints 
    app.register_blueprint(cards_bp)
    app.register_blueprint(boards_bp)

    CORS(app)
    return app
