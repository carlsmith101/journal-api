"""
"""


from flask import Blueprint, request
from flask_restx import Resource, Api, fields

from src import db
from src.api.models import Entry
from sqlalchemy.sql import func


entries_blueprint = Blueprint('entries', __name__)
api = Api(entries_blueprint)

entry = api.model('Entry', {
    'content': fields.String(required=True),
    'entry_date': fields.Date
})


class EntriesList(Resource):

    @api.marshal_with(entry, as_list=True)
    def get(self):
        return Entry.query.all(), 200

    @api.expect(entry, validate=True)
    def post(self):
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


api.add_resource(EntriesList, '/entries')

class Entries(Resource):

    @api.marshal_with(entry)
    def get(self, date):
        entry = Entry.query.filter_by(entry_date=date).first()

        if not entry:
            api.abort(404, f'Journal entry on date {date} does not exist')
        
        return entry, 200


api.add_resource(Entries, '/entries/<date>')
