"""
ping

This module defines the API resource and endpoint for checking the status of the API.

"""


from flask import Blueprint
from flask_restx import Resource, Api

# add blueprint
ping_blueprint = Blueprint('ping', __name__)
api = Api(ping_blueprint)


class Ping(Resource):
    """
    Ping Resource

    This resource is used to check the status of the API.
    
    """

    def get(self):
        """
        Retrieve health status of the API.

        """

        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')
