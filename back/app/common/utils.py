'''Utility functions

This module contains general functions to simplifiy certain operations
'''
import os

from . import constants

def get_url_prefix(u):
    return os.path.join(constants.url_prefix, u)

def check_api_version_number(vn):
    '''Ensure that API_VERSION_NUMBER_STR conforms to desired value'''
    if not isinstance(vn, str):
        raise ValueError("version number must be of type str")
    if '.' not in vn:
        raise ValueError("version number must contain a decimal")
