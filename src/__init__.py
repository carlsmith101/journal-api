"""
Journal API

A RESTful API for a journal application built using Flask and Flask-RESTX.

For more information, refer to the documentation or visit the [project repository](https://github.com/carlsmith101/journal-api).

"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instantiate the db
db = SQLAlchemy()


def create_app(script_info=None):
    """
    Create and configure the Flask application.
    
    """

    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from src.api.entries import entries_blueprint
    app.register_blueprint(entries_blueprint) 
    from src.api.ping import ping_blueprint   
    app.register_blueprint(ping_blueprint, url_prefix='/health')
    
    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
