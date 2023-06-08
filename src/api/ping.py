"""
"""


from flask import Blueprint
from flask_restx import Resource, Api


ping_blueprint = Blueprint('ping', __name__)
api = Api(ping_blueprint)


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
