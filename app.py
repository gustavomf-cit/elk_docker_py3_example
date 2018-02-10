#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# app.py
# @Author : Gustavo M Freitas (gustavomf@ciandt.com)
# @Link   : https://github.com/gustavomf-cit
# @Date   : 2/9/2018, 9:56:28 AM

from models import logger
from flask import Flask
import json
# https://github.com/vklochan/python-logstash

app = Flask(__name__)

# add extra field to logstash message
extra = {
    "type": "testing",
    "lambda_name": "appname-test",
    "lambda_version": "1.0.0"
}


@app.route('/')
def hello_world():
    logger.error({"account": 123,
                  "logger_name": "appname",
                  "ip": "172.20.19.18"}, extra=extra)
    return json.dumps({'mes': 'ola'}), 200


app.run(port=8080)
