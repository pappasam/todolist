'''Utility functions

This module contains general functions to simplifiy certain operations
'''

import itertools as it

def getbool(d, k, default):
    '''With dict and key with str true/false, translate to BOOL

    Return corresponding BOOL, or default value if unable to translate

    :d: DICT
    :k: STR dictionary key that is assumed to contain 'true' or 'false'
    :default: default value to return if can't find 'true' or 'false'
    '''
    v = d.get(k, None)
    vc = (  # val-condition
        (v == 'true', lambda: v in ('true', 'false')),
        (v, lambda: isinstance(v, bool)),
        (default, lambda: True),
    )
    return next(it.dropwhile(lambda t: not t[1](), vc))[0]
