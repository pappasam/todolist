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
        '''Retrive all notes and all content

        Return json with list of notes
        '''
        db_query_results = Notes.query.all()
        notes = self.schema.dump(db_query_results, many=True).data
        return jsonify({"notes": notes})

    def post(self):
        '''Add new note to database

        Return json value for the note's value
        '''
        js_data = request.get_json(force=True)
        notes_entry = Notes(**js_data)
        db.session.add(notes_entry)
        db.session.commit()
        note_json = self.schema.dump(notes_entry).data
        return jsonify({"note": note_json})

    def patch(self):
        '''Update the content of a note

        Return json value for old note's value
        '''
        js_data = request.get_json(force=True)
        note = Notes.query.filter_by(id=js_data['id']).first()
        note_content_original = self.schema.dump(note).data
        note.content = js_data['content']
        note_content_new = self.schema.dump(note).data
        db.session.commit()
        return jsonify({
            'note_original': note_content_original,
            'note_new': note_content_new,
        })

resources = OrderedDict()
resources['/notes'] = ApiNotes
