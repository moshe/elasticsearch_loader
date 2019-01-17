#!/usr/bin/env python
# -*- coding: utf-8 -*-
import click
from elasticsearch_loader import load
import redis
import json


def redis_list_iterator(redis_connection, list_name):
    while True:
        yield json.loads(redis_connection.blpop(list_name)[1])


def register(cli):
    @cli.command(name='redis')
    @click.argument('list_name', type=str, nargs=1, required=True)
    @click.pass_context
    def _redis(ctx, list_name):
        if not redis:
            raise SystemExit("redis module not found, please install manually")

        conn = redis.Redis()
        load(redis_list_iterator(conn, list_name), ctx.obj)
