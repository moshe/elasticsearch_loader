from click.testing import CliRunner
from elasticsearch_loader import cli
import mock


def invoke(*args, **kwargs):
    content = """id,first,last\nMOZA,Moshe,Zada\nMICHO,Michelle,Obama\na,b,c\nf,g,h"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('sample.csv', 'w') as f:
            f.write(content)
        return runner.invoke(*args, **kwargs)


@mock.patch('elasticsearch_loader.single_bulk_to_es')
def test_should_iterate_over_csv(bulk):
    result = invoke(cli, ['--index=index', '--type=type', 'csv', 'sample.csv'], catch_exceptions=False)
    assert result.exit_code == 0
    assert filter(None, bulk.call_args[0][0]) == ({'first': 'Moshe', 'id': 'MOZA', 'last': 'Zada'},
                                                  {'first': 'Michelle', 'id': 'MICHO', 'last': 'Obama'},
                                                  {'first': 'b', 'id': 'a', 'last': 'c'},
                                                  {'first': 'g', 'id': 'f', 'last': 'h'})


@mock.patch('elasticsearch_loader.single_bulk_to_es')
def test_should_iterate_over_csv_bulk_size_1(bulk):
        result = invoke(cli, ['--bulk-size=1', '--index=index', '--type=type', 'csv', 'sample.csv'], catch_exceptions=False)
        assert result.exit_code == 0
        assert bulk.call_count == 2
        assert filter(None, bulk.call_args[0][0]) == ({'first': 'g', 'id': 'f', 'last': 'h'},)
