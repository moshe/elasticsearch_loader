from itertools import zip_longest as zip_longest

from .parsers import json


def grouper(iterable, n, fillvalue=None):
    'Collect data into fixed-length chunks or blocks'
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def bulk_builder(bulk, config):
    for item in [_f for _f in bulk if _f]:
        source = item
        if config['keys']:
            source = {x: y for x, y in list(item.items()) if x in config['keys']}

        body = {'_index': config['index'],
                '_type': config['type'],
                '_source': source}

        if config['id_field']:
            body['_id'] = item[config['id_field']]

            if config['as_child']:
                body['_parent'] = body['_id']
                body['_routing'] = body['_id']

        if config['update']:
            # default _op_type is 'index', which will overwrites existing doc
            body['_op_type'] = 'update'
            body['doc'] = source
            del body['_source']

        if config['pipeline']:
            body['pipeline'] = config['pipeline']

        yield body


def json_lines_iter(fle):
    for line in fle:
        yield json.loads(line)
