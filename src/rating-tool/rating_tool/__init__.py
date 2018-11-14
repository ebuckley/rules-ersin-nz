import os
from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='postgresql://postgres:mysecretpassword@localhost:5432/environmentcanterbury',
        DATABASE_PASSWORD='mysecretpassword'
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import (geometry, rules)
    app.register_blueprint(geometry.bp)
    app.register_blueprint(rules.bp)


    return app