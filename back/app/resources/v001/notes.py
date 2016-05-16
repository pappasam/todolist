import flask_restful

from collections import OrderedDict
from flask_restful import Api, Resource, reqparse, inputs
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from .extensions import ext
from .models import Notes, NotesSchema
from .utils import getbool

db = ext['db']

class NotesParser(object):
    '''Parser arguments for Notes api'''

    parser_post = reqparse.RequestParser(bundle_errors=True)
    parser_post.add_argument(
        'completed', type=inputs.boolean,
        required=True, location='json'
    )
    parser_post.add_argument(
        'text', type=str,
        required=True, location='json'
    )

    parser_patch = parser_post.copy()
    parser_patch.add_argument(
        'id', type=int,
        required=True, location='json'
    )

class NotesApi(Resource, NotesParser):
    '''Operations on note data'''

    schema = NotesSchema()

    def get(self):
        '''Retrive all notes and all text

        Return json with list of notes
        '''
        db_query_results = Notes.query.all()
        notes = self.schema.dump(db_query_results, many=True).data
        return jsonify(response='ok', data={"notes": notes})

    def post(self):
        '''Add new note to database

        Return json value for the note's value
        '''
        args = self.parser_post.parse_args()
        notes_entry = Notes(**args)
        db.session.add(notes_entry)
        db.session.commit()
        note_json = self.schema.dump(notes_entry).data
        return jsonify(response='ok', data={"note": note_json})

    def patch(self):
        '''Update the text and/or completed status of a note

        Return json value for old note's value
        '''
        args = self.parser_patch.parse_args()
        note = Notes.query.filter_by(id=args['id']).first()
        note.text = args['text']  # Mutation begin
        note.completed = args['completed']
        db.session.commit()  # Mutation end
        return jsonify(response='ok')

resources = OrderedDict()
resources['/notes'] = NotesApi
