from flask import Blueprint, jsonify, request
from flask_restful import Api

from ...common.utils import get_url_prefix, check_api_version_number

from .notes import NotesApi

#######################################################################
# Hard-coded constants
#######################################################################
API_VERSION_NUMBER_STR = '1.0'

#######################################################################
# Calculated constants
#######################################################################
check_api_version_number(API_VERSION_NUMBER_STR)
bp_name = 'v{}'.format(
    API_VERSION_NUMBER_STR[:API_VERSION_NUMBER_STR.find('.')]
)
bp_url_prefix = get_url_prefix('v{}'.format(API_VERSION_NUMBER_STR))

#######################################################################
# Blueprint and Api
#######################################################################
bp = Blueprint(bp_name, __name__)
api = Api(bp, prefix=bp_url_prefix)

#######################################################################
# Assemble resources
#######################################################################
api.add_resource(NotesApi, '/notes')
