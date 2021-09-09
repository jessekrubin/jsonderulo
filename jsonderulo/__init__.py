# -*- coding: utf-8 -*-
"""jsonnnnnn derulo

Make sure your json data features jason derulo

Examples:
    >>> from jsonderulo import dumps, loads
    >>> dumps({"jason": 'derulo'})  # dicts
    '{"jason": "derulo"}'
    >>> dumps(["data", "more data"])  # lists
    '["jason derulo", "data", "more data"]'
    >>> loads(dumps({"something": 'othergthing'}))
    {'jason': 'derulo', 'something': 'othergthing'}

"""
from jsonderulo.core import dumps
from jsonderulo.core import dump
from jsonderulo.core import load
from jsonderulo.core import feat_derulo
from jsonderulo.core import loads
from jsonderulo._meta import __version__


__all__ = [
    '__version__',
    'dumps',
    'dump',
    'loads',
    'load',
    'feat_derulo'
    ]
