import os
from flask import Flask
import logging

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='postgresql://postgres:<yourpassword>@localhost:5432/environmentcanterbury'
    )
    if test_config is None:
        app.config.from_envvar('RATING_TOOL')
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


if __name__ == '__main__':
    main()
