"""
entries

This module defines the API resources and endpoints for managing journal entries.

"""


from flask import Blueprint, request
from flask_restx import Resource, Api, fields

from src import db
from src.api.models import Entry
from sqlalchemy.sql import func

# add blueprint
entries_blueprint = Blueprint('entries', __name__)
api = Api(entries_blueprint)

# define resource fields
resource_fields = api.model('Entry', {
    'content': fields.String(required=True),
    'entry_date': fields.Date
})


class EntriesList(Resource):
    """
    EntriesList Resource

    Represents a collection of journal entries. Handles the endpoints for retrieving and creating journal entries.

    """

    @api.marshal_with(resource_fields, as_list=True)
    def get(self):
        """
        Retrieve all journal entries.

        """

        return Entry.query.all(), 200

    @api.expect(resource_fields, validate=True)
    def post(self):
        """
        Add a new journal entry.

        """

        post_data = request.get_json()
        content = post_data.get('content')
        response_object = {}

        existing_entry = Entry.query.filter_by(entry_date=func.current_date()).first()

        if existing_entry:
            response_object['message'] = 'A journal entry already exists for today'
            return response_object, 400

        db.session.add(Entry(content=content))
        db.session.commit()

        response_object['message'] = 'Journal entry added successfully'
        return response_object, 201


class Entries(Resource):
    """
    Entries Resource
    
    This resource represents a single journal entry and handles the endpoint for retrieving a single journal entry.

    """

    @api.marshal_with(resource_fields)
    def get(self, date):
        """
        Retrieve a journal entry by date.

        """

        entry = Entry.query.filter_by(entry_date=date).first()

        if not entry:
            api.abort(404, f'Journal entry on date {date} does not exist')
        
        return entry, 200


api.add_resource(EntriesList, '/entries')
api.add_resource(Entries, '/entries/<date>')
