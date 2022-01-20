import views
from flask import Flask

def create_app():
    app = Flask(__name__)
    views.configure(app)
    return app

