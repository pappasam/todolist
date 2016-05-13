import flask_restful

from flask_restful import Api, Resource
from flask import jsonify, request
from SQLAlchemy.exc import SQLAlchemyError

from .extensions import ext
from .models import Notes, NotesSchema

db = ext['db']
