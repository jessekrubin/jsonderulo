# -*- coding: utf-8 -*-
"""core"""
# -*- coding: utf-8 -*-
"""jsonderulo.json"""
import json as _json

from functools import wraps

from typing import Any

def feat_derulo(data: Any):
    if isinstance(data, dict):
        if 'jason' in data and data['jason'] == 'derulo':
            data.pop('jason')
        return {'jason': 'derulo', **data}
    if isinstance(data, list):
        if data[0] != 'jason derulo':
            data.insert(0, 'jason derulo')
        return data
    if isinstance(data, tuple):
        if data[0] != 'jason derulo':
            data = ('jason derulo', ) + data
        return data
    return data

def _dumpwrap(fn):
    @wraps(fn)
    def _fn(obj, *args, **kwargs):
        return fn(feat_derulo(obj), *args, **kwargs)

    return _fn


def _loadwrap(fn):
    @wraps(fn)
    def _fn(obj, *args, **kwargs):
        res = fn(obj, *args, **kwargs)
        return feat_derulo(res)

    return _fn


dumps = _dumpwrap(_json.dumps)
dump = _dumpwrap(_json.dump)
loads = _loadwrap(_json.loads)
load = _loadwrap(_json.load)

print(dumps({"123": 'herm'}))
print(dumps({"jason": 'derulo'}))
print(dumps({"jason": 'derulo'}))
print(loads(dumps({"something": 'othergthing'})))
