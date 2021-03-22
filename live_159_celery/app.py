# from tasks import ola_mundo

# ola_mundo.delay()

from dataclasses import dataclass
from httpx import post
from base64 import standard_b64encode

@dataclass
class Pessoa:
    nome: str
    telefone: str
    documento: str

def cadastro(pessoa: Pessoa):
    documento = open(pessoa.documento, 'rb').read()

    image = standard_b64encode(documento).decode('utf-8')

    data = {
        'image': image
    }
    response = post(
            'http://live-159-external.herokuapp.com/document-to-text',
            json=data,
            timeout=None
    )
    print(response.json())

p = Pessoa('Eduardo', '12314124123','images/documento_errado.png')

cadastro(p)

