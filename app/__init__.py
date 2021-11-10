from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config: str):
    """Create instance of Flask application with config for dev, test, or prod"""
    application = Flask(__name__)
    configuration = Path.joinpath(Path.cwd(), 'config', config + '.py')
    # configuration = os.path.join(os.getcwd(), 'config', config + '.py')
    application.config.from_pyfile(configuration)

    db.init_app(application)

    from app.catalog import main
    application.register_blueprint(main)

    return application
