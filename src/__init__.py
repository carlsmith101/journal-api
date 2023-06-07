"""
Journal API

This is the API for the journal application

For more information, refer to the documentation or visit the project repository at: https://github.com/carlsmith101/journal-api
"""

import os


from flask import Flask, jsonify
from flask_restx import Resource, Api


# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


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
