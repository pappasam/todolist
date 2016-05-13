import flask_restful

from collections import OrderedDict
from flask_restful import Api, Resource
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from .extensions import ext
from .models import Notes, NotesSchema

db = ext['db']

class ApiNotes(Resource):
    '''Operations on note data'''

    schema = NotesSchema()

    def get(self):
        db_query_results = Notes.query.all()
        notes = self.schema.dump(db_query_results, many=True).data
        return jsonify({"notes": notes})

    def post(self):
        '''Add new entry to database

        Return json value for the note
        '''
        js_data = request.get_json(force=True)
        notes_entry = Notes(**js_data)
        db.session.add(notes_entry)
        db.session.commit()
        note_json = self.schema.dump(notes_entry).data
        return jsonify({"note": note_json})

resources = OrderedDict()
resources['/notes'] = ApiNotes
