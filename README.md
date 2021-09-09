# jsonderulo

Make sure your 'jason derulo' is featured as the first part of your json data

[![Wheel](https://img.shields.io/pypi/wheel/jsonderulo.svg)](https://img.shields.io/pypi/wheel/jsonderulo.svg)
[![Version](https://img.shields.io/pypi/v/jsonderulo.svg)](https://img.shields.io/pypi/v/jsonderulo.svg)
[![py_versions](https://img.shields.io/pypi/pyversions/jsonderulo.svg)](https://img.shields.io/pypi/pyversions/jsonderulo.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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


## TODO

 [] polyfill/patch json module fn
 [] Add support for 'DJ Khaled'
