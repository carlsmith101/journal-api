"""
Journal API

This is the API for the journal application

For more information, refer to the documentation or visit the project repository at: https://github.com/carlsmith101/journal-api
"""

import os
import uuid


from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)


class Entry(db.Model):
    """
    
    """
    __tablename__ = 'entries'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    content = db.Column(db.String(2000), nullable=False)
    date = db.Column(db.Date, nullable=False, unique=True, default=db.func.current_date())

    def __init__(self, content):
        self.content = content


class Ping(Resource):
    """
    Ping Resource

    This resource is used to check the status of the API.
    
    """

    def get(self):
        """
        Handle GET request for ping.

        Returns:

            A dictionary with the status and message of the ping response.

                - status (str): The status of the ping response. Always set to 'success'.
                - message (str): The message indicating a successful ping. Always set to 'pong!'.
        """
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')
