from pathlib import Path

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config: str):
    """Create instance of Flask application with config for dev, test, or prod"""
    application = Flask(__name__)
    configuration = Path.joinpath(Path.cwd(), 'config', config + '.py')
    application.config.from_pyfile(configuration)

    db.init_app(application)  # bind database to flask application
    bootstrap.init_app(application)  # initialize bootstrap
    login_manager.init_app(application)  # initialize login manager
    bcrypt.init_app(application)  # initialize bcrypt

    from app.catalog import main
    application.register_blueprint(main)

    from app.auth import authentication
    application.register_blueprint(authentication)

    return application
