#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from subprocess import check_call

matrix = yaml.safe_load(open('./.travis.yml'))['env']['matrix']
for case in matrix:
    print("-" * 15 + case + "-" * 15)
    check_call("{} docker-compose rm -f".format(case), shell=True)
    check_call("{} docker-compose up --build --abort-on-container-exit".format(case), shell=True)
