from flask import jsonify, render_template

def configure(app):
    @app.route("/")
    def index():
        return "<p>Hello, Simon!</p>"
    @app.route("/api")
    def api():
        return jsonify(data = {'nome': 'Dimas'})
    @app.route("/langs")
    def langs():
        ling = ['Python', 'Bash', 'C++', 'Java']
        return render_template(
            'index.html',
            titulo = "Melhores Linguagens",
            linguagens = ling
        )

