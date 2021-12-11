# -*- coding: utf-8 -*-
"""Имитация настоящего приложения.
"""

from flask import Flask

app = Flask(__name__)


@app.get('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()
