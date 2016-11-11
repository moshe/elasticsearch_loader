# elasticsearch_loader [![Build Status](https://travis-ci.org/Moshe/elasticsearch_loader.svg?branch=master)](https://travis-ci.org/Moshe/elasticsearch_loader) [![Can I Use Python 3?](https://caniusepython3.com/project/elasticsearch-loader.svg)](https://caniusepython3.com/project/elasticsearch-loader) [![PyPI version](https://badge.fury.io/py/elasticsearch_loader.svg)](https://pypi.python.org/pypi/elasticsearch-loader)

### Main features:
* Batch upload CSV (actually any *SV) files to Elasticsearch
* Batch upload JSON files / JSON lines to Elasticsearch
* Batch upload parquet files to Elasticsearch
* Pre defining custom mappings
* Delete index before upload
* Index documents with _id from the document itself
* Load data directly from url
* Supports ES 1.X, 2.X and 5.X
* And more

### Installation
`
pip install elasticsearch-loader
`  
*In order to add parquet support run `pip install elasticsearch-loader[parquet]`*


### Usage
```
(venv)/tmp $ elasticsearch_loader --help
Usage: elasticsearch_loader [OPTIONS] COMMAND [ARGS]...

Options:
  --bulk-size INTEGER             How many docs to collect before writing to
                                  ElasticSearch
  --concurrency INTEGER           How much worker threads to start
  --es-host TEXT                  Elasticsearch cluster entry point. eg.
                                  http://localhost:9200
  --index TEXT                    Destination index name  [required]
  --delete                        Delete index before import?
  --type TEXT                     Docs type  [required]
  --id-field TEXT                 Specify field name that be used as document
                                  id
  --index-settings-file FILENAME  Specify path to json file containing index
                                  mapping and settings
  --help                          Show this message and exit.

Commands:
  csv
  json     FILES with the format of [{"a": "1"}, {"b":...
  parquet
```

### Examples
#### Load 2 CSV files
`elasticsearch_loader --index incidents --type incident csv file1.csv file2.csv`

#### Load JSON files
`elasticsearch_loader --index incidents --type incident json *.json`

#### Load all git commits into elasticsearch
`git log  --pretty=format:'{"sha":"%H","author_name":"%aN", "author_email": "%aE","date":"%ad","message":"%f"}' | elasticsearch_loader --type git --index git json --json-lines -`

#### Load parquet file
`elasticsearch_loader --index incidents --type incident parquet file1.parquet`

#### Load CSV from github repo (actually any http/https is ok)
`elasticsearch_loader --index data --type avg_height --id-field country json https://raw.githubusercontent.com/samayo/country-data/master/src/country-avg-male-height.json`

#### Load data from stdin
`generate_data | elasticsearch_loader --index data --type incident csv -`

#### Read _id from incident_id field
`elasticsearch_loader --id-field incident_id --index incidents --type incident csv file1.csv file2.csv`

#### Change bulk size
`elasticsearch_loader --bulk-size 300 --index incidents --type incident csv file1.csv file2.csv`

#### Change index concurrency
`elasticsearch_loader --concurrency 20 --index incidents --type incident csv file1.csv file2.csv`

#### Load custom mappings
`elasticsearch_loader --index-settings-file samples/mappings.json --index incidents --type incident csv file1.csv file2.csv`

### Tests and sample data
Tests are located under test and can run by runnig `tox`
input format can be found under samples

### TODO
- [x] parquet support
- [x] progress bar
- [ ] DLQ style out file for docs that didn't got in
- [x] Python3 support
- [x] pep8 test
