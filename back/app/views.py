import flask_restful

from collections import OrderedDict
from flask_restful import Api, Resource
from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from .extensions import ext
from .models import Notes, NotesSchema
from .utils import getbool

db = ext['db']

class ApiNotes(Resource):
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
        js_data = request.get_json(force=True)
        # Begin Mutation
        js_data['completed'] = getbool(js_data, 'completed', False)
        # End Mutation
        notes_entry = Notes(**js_data)
        # Begin Mutation
        db.session.add(notes_entry)
        db.session.commit()
        # End Mutation
        note_json = self.schema.dump(notes_entry).data
        return jsonify(response='ok', data={"note": note_json})

    def patch(self):
        '''Update the text and/or completed status of a note

        Return json value for old note's value
        '''
        js_data = request.get_json(force=True)
        note = Notes.query.filter_by(id=js_data['id']).first()
        # Begin Mutation
        note.text = js_data.get('text', note.text)
        note.completed = getbool(js_data, 'completed', note.completed)
        db.session.commit()
        # End Mutation
        return jsonify(response='ok')

resources = OrderedDict()
resources['/notes'] = ApiNotes
