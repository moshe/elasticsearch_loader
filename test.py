#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
from subprocess import check_call

matrix = yaml.load(file('./.travis.yml'))['env']['matrix']
for case in matrix:
    check_call("{} docker-compose up --build --abort-on-container-exit".format(case), shell=True)
