from flask import Flask
from generatorpass.ext import site
from generatorpass.ext import config
from generatorpass.ext import toolbar



def create_app():
    app = Flask(__name__)
    site.init_app(app)
    config.init_app(app)
    toolbar.init_app(app)
    return app
