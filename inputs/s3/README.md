# esl-s3
Plugin for listing and indexing files from S3

## Installation
`pip install esl-s3`

## Usage
```
$ elasticsearch_loader --index lol --type cake s3 --help
Usage: elasticsearch_loader s3 [OPTIONS] BUCKET

Options:
  --prefix TEXT  AWS_S3_PREFIX
    -h, --help     Show this message and exit.
```

## Examples
`elasticsearch_loader --index index --type type s3 mybucket`
