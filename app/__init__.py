"""
The flask application package.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config

db = SQLAlchemy()
login_manager = LoginManager();

def create_app (config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "index"

    migrate = Migrate(app, db)

    from app import models

    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    return app