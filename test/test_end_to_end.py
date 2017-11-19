from click.testing import CliRunner
from elasticsearch_loader import cli
from elasticsearch import Elasticsearch

es = Elasticsearch('elasticsearch')


def invoke(*args, **kwargs):
    content = """id,first,last\nMOZA,Moshe,Zada\nMICHO,Michelle,Obama\na,b,c\nf,g,h"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('sample.csv', 'w') as f:
            f.write(content)
        result = runner.invoke(*args, **kwargs)
        assert result.exit_code == 0
        es.indices.flush_synced()
        return result


def test_should_load_and_searchable():
    invoke(cli, ['--index=index', '--delete', '--type=type', 'csv', 'sample.csv'], catch_exceptions=False)
    assert es.search(index='index', body={"query": {"bool": {"filter": [{"match": {"first": "Moshe"}}]}}})['hits']['total'] == 1
    assert es.search(index='index', body={"query": {"bool": {"filter": [{"match": {"last": "zada"}}]}}})['hits']['total'] == 1
    assert es.search(index='index', body={"query": {"bool": {"filter": [{"match": {"first": "Michelle"}}]}}})['hits']['total'] == 1


def test_should_load_from_id():
    invoke(cli, ['--index=index', '--delete', '--type=type', '--id-field=id', 'csv', 'sample.csv'], catch_exceptions=False)
    assert es.get(index='index', doc_type='type', id='MOZA')['found'] is True
    assert es.get(index='index', doc_type='type', id='MICHO')['found'] is True
    assert es.get(index='index', doc_type='type', id='a')['found'] is True
    assert es.get(index='index', doc_type='type', id='f')['found'] is True
