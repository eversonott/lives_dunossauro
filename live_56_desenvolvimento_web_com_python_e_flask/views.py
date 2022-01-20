from flask import jsonify

def configure(app):
    @app.route("/")
    def index():
        return "<p>Hello, Simon!</p>"
    @app.route("/api")
    def api():
        return jsonify(data = {'nome': 'Dimas'})

