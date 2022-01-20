import views
import contact
from flask import Flask

def create_app():
    app = Flask(__name__)
    views.configure(app)
    # configurar extens√es
    contact.configure(app)
    # configurar as vari√veis
    return app

