try:
    from itertools import izip_longest as zip_longest
except ImportError:
    from itertools import zip_longest

from .parsers import json


def grouper(iterable, n, fillvalue=None):
    'Collect data into fixed-length chunks or blocks'
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def bulk_builder(bulk, config):
    for item in filter(None, bulk):
        body = {'_index': config['index'],
                '_type': config['type'],
                '_source': item}
                
        if config['id_field']:
            body['_id'] = item[config['id_field']]
            
            if config['as_child']:
                body['_parent'] = body['_id']
                body['_routing'] = body['_id']
            
        yield body


def json_lines_iter(fle):
    for line in fle:
        yield json.loads(line.decode('utf-8'))
