#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
from elasticsearch_loader import load
import redis
import json


def redis_list_iterator(redis_connection, list_names, list_read_timeout):
    while True:
        item = redis_connection.blpop(list_names, list_read_timeout)
        if item is None:
            return
        yield json.loads(item[1])


@click.option('--host', default='localhost', help='Redis host', envvar='REDIS_HOST')
@click.option('--port', default=6379, type=int, help='Redis port', envvar='REDIS_PORT')
@click.option('--db', default=0, type=int, help='Redis db', envvar='REDIS_DB')
@click.option('--list-read-timeout', default=0, type=int,
              help='block for X seconds, or until a value gets pushed on to one of the lists. If timeout is 0, then block indefinitely.')
@click.argument('list_names', type=str, nargs=-1, required=True)
@click.pass_context
def _redis(ctx, host, port, db, list_read_timeout, list_names):
    conn = redis.Redis(host=host, port=port, db=db)
    load(redis_list_iterator(conn, list_names, list_read_timeout), ctx.obj)


def register():
    return 'redis', _redis
