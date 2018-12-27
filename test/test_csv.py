#!/usr/bin/env python
# -*- coding: utf-8 -*-

from click.testing import CliRunner
from elasticsearch_loader import cli
import mock
import sys


def invoke(*args, **kwargs):
    content = u"""id,first,last\nMOZA,Moshe,Zada\nMICHO,Michelle,Obama\na,b,c\nf,g,א"""
    if sys.version_info[0] == 2:
        content = content.encode('utf-8')
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('sample.csv', 'w') as f:
            f.write(content)
        return runner.invoke(*args, **kwargs)


@mock.patch('elasticsearch_loader.single_bulk_to_es')
def test_should_iterate_over_csv(bulk):
    result = invoke(cli, ['--index=index', '--type=type', 'csv', 'sample.csv'], catch_exceptions=False)
    assert result.exit_code == 0
    assert [x for x in bulk.call_args[0][0] if x is not None] == [{'first': 'Moshe', 'id': 'MOZA', 'last': 'Zada'},
                                                                  {'first': 'Michelle', 'id': 'MICHO', 'last': 'Obama'},
                                                                  {'first': 'b', 'id': 'a', 'last': 'c'},
                                                                  {'first': 'g', 'id': 'f', 'last': u'א'}]
