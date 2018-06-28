# elasticsearch_loader [![Build Status](https://travis-ci.org/moshe/elasticsearch_loader.svg?branch=master)](https://travis-ci.org/moshe/elasticsearch_loader) [![Can I Use Python 3?](https://caniusepython3.com/project/elasticsearch-loader.svg)](https://caniusepython3.com/project/elasticsearch-loader) [![PyPI version](https://badge.fury.io/py/elasticsearch_loader.svg)](https://pypi.python.org/pypi/elasticsearch-loader)

### Main features:
* Batch upload CSV (actually any *SV) files to Elasticsearch
* Batch upload JSON files / JSON lines to Elasticsearch
* Batch upload parquet files to Elasticsearch
* Pre defining custom mappings
* Delete index before upload
* Index documents with _id from the document itself
* Load data directly from url
* SSL and basic auth

### Test matrix
|python / es| 2.4.6 | 5.6.5 | 6.3.0 |
| ----- | ----- |------ | ----- |
|2.7|V|V|V|
|3.6|V|V|V|

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
  -c, --config-file TEXT          Load default configuration file from esl.yml
  --bulk-size INTEGER             How many docs to collect before writing to
                                  ElasticSearch (default 500)
  --es-host TEXT                  Elasticsearch cluster entry point. (default
                                  http://localhost:9200)
  --verify-certs                  Make sure we verify SSL certificates
                                  (default false)
  --use-ssl                       Turn on SSL (default false)
  --ca-certs TEXT                 Provide a path to CA certs on disk
  --http-auth TEXT                Provide username and password for basic auth
                                  in the format of username:password
  --index TEXT                    Destination index name  [required]
  --delete                        Delete index before import? (default false)
  --progress                      Enable progress bar - NOTICE: in order to
                                  show progress the entire input should be
                                  collected and can consume more memory than
                                  without progress bar
  --type TEXT                     Docs type  [required]
  --id-field TEXT                 Specify field name that be used as document
                                  id
  --as-child                      Insert _parent, _routing field, the value is 
                                  same as _id. Note: must specify --id-field
                                  explicitly
  --with-retry                    Retry if ES bulk insertion failed
  --index-settings-file FILENAME  Specify path to json file containing index
                                  mapping and settings, creates index if
                                  missing
  -h, --help                      Show this message and exit.

Commands:
  csv
  json       FILES with the format of [{"a": "1"}, {"b": "2"}]
  parquet
```

### Examples
#### Load 2 CSV to elasticsearch
`elasticsearch_loader --index incidents --type incident csv file1.csv file2.csv`

#### Load JSONs to elasticsearch
`elasticsearch_loader --index incidents --type incident json *.json`

#### Load all git commits into elasticsearch
`git log  --pretty=format:'{"sha":"%H","author_name":"%aN", "author_email": "%aE","date":"%ad","message":"%f"}' | elasticsearch_loader --type git --index git json --json-lines -`

#### Load parquet to elasticsearch
`elasticsearch_loader --index incidents --type incident parquet file1.parquet`

#### Load CSV from github repo (actually any http/https is ok)
`elasticsearch_loader --index data --type avg_height --id-field country json https://raw.githubusercontent.com/samayo/country-data/master/src/country-avg-male-height.json`

#### Load data from stdin
`generate_data | elasticsearch_loader --index data --type incident csv -`

#### Read id from incident_id field
`elasticsearch_loader --id-field incident_id --index incidents --type incident csv file1.csv file2.csv`

#### Load custom mappings
`elasticsearch_loader --index-settings-file samples/mappings.json --index incidents --type incident csv file1.csv file2.csv`

### Tests and sample data
End to end and regression tests are located under test directory and can run by runnig `./test.py`
Input formats can be found under samples
