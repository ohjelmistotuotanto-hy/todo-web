from flask import Flask
from database import db
from config import DATABASE_URL
from controllers.todos_controller import todos_controller

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(todos_controller)

    db.init_app(app)

    return app
