from flask import Flask, render_template, request
from wtforms import Form, validators
from wtforms.fields import EmailField, StringField, PasswordField, SubmitField, RadioField, SelectField

app = Flask('meuapp')

class FormCadastro(Form):
    nome = StringField('Nome: ')
    email = EmailField('Email')
    pergunta = RadioField('Você gosta mais de', choices=['Batata', 'Estudar'])
    escolha = SelectField('Escolha', choices=['Cerveja', 'Café'])
    senha = PasswordField(
        'Sua senha :',
        [
            validators.EqualTo(
                'senha_confirm', 
                message='As senhas são diferentes'
            ),
            validators.Length(
                min=6, 
                max=20, 
                message='O campo deve ter entre %(min)d e %(max)d caracteres.')
        ]
    )
    senha_confirm = PasswordField('Confirme sua senha: ')
    btn = SubmitField('Criar')
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = FormCadastro(request.form)
    if request.method == 'POST' and form.validate():
        return 'OK'
    return render_template(
            'cadastro.html',
            form=form
    )
app.run()
