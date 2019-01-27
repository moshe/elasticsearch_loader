# esl-redis
Read continuously from a redis list(s) and index to elasticsearch

## Installation
`pip install esl-redis`

## Usage
```
$ elasticsearch_loader --index lol --type cake redis --help
Usage: elasticsearch_loader redis [OPTIONS] LIST_NAMES...

Options:
  --host TEXT                  Redis host
  --port INTEGER               Redis port
  --db INTEGER                 Redis db
  --list-read-timeout INTEGER  block for X seconds, or until a value gets
                               pushed on to one of the lists. If timeout is 0,
                               then block indefinitely.
  -h, --help                   Show this message and exit.
```

## Examples
`elasticsearch_loader --index index --type type redis my_list_name`
