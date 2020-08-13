from flask import Flask
from generatorpass.ext import site
from generatorpass.ext import config
from generatorpass.ext import toolbar
from generatorpass.ext import db
from generatorpass.ext import cli



def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
