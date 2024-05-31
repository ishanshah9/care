import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .momentum_orm import base_user


### need to code util file and the config file. 
from .util import get_config

import click
from flask import Flask

app = Flask(__name__)

# before running the init-db command in the terminal we need to set the FLASK_ENV

# $ export FLASK_APP=server.prepare_orm
# $ export FLASK_ENV=dev_lite
# $ export LC_ALL=C.UTF-8 && export LANG=C.UTF-8
# $ pipenv run flask init-db


@app.cli.command('init-db')
def init_db():
    config = get_config(os.environ['FLASK_ENV'], open('server/config.yaml'))
    db   = create_engine(config['DB'])
    base_user.metadata.create_all(db)