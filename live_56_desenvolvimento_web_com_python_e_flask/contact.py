from flask import Blueprint, render_template, request


bp = Blueprint('contact', __name__, url_prefix = '/contact')

@bp.route('/', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

    print(request.form)
    nome = request.form.get('nome')
    mensagem = request.form.get('mensagem')
    print(nome)
    return f"Olá {nome}. Sua mensagem foi enviada"

def configure(app):
    app.register_blueprint(bp)
