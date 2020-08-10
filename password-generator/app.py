from flask import Flask



def create_app():
    app = Flask(__name__)
    site.init_app(app)
    return app
