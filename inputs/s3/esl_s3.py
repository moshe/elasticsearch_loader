#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
import boto3

from elasticsearch_loader import load
from elasticsearch_loader.parsers import json


def s3_iterator(bucket):
    for key in bucket.objects.all():
        yield json.load(key.get()['Body'])


@click.option('--prefix', default='', help='AWS_S3_PREFIX', envvar='ESL_S3_PREFIX')
@click.argument('bucket', type=str, nargs=1, required=True)
@click.pass_context
def _s3(ctx, prefix, bucket):
    s3 = boto3.resource('s3')
    bucket_obj = s3.Bucket(bucket)
    load(s3_iterator(bucket_obj), ctx.obj)


def register():
    return 's3', _s3
