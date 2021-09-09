# jsonderulo

Make sure your json data features 'jason derulo'

## Install:

```
pip install jsonderulo
poetry add jsonderulo 
```

## Usage:

```python
>>> from jsonderulo import dumps, loads, load, dump
>>> dumps({"jason": 'derulo'})  # dicts
'{"jason": "derulo"}'
>>> dumps(["data", "more data"])  # lists
'["jason derulo", "data", "more data"]'
>>> loads(dumps({"something": 'othergthing'}))
{'jason': 'derulo', 'something': 'othergthing'}
```
