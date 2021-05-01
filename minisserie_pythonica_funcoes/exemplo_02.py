
# Função anonima com paramentro

anonima = lambda param: param + 2

anonima_plus = lambda param1, param2: param1 + param2

# Função nominal com parametros

def soma_posisiconal(x, y):
    """x e y são parametros posicionais."""
    return x + y
def soma_nomeados(x=7, y=7):
    """x e y são parametros nomeados

    Na falta de x ou y o valor 7 será usado
    """
    print(f'x: {x}, y: {y}')
    return x + y


def soma_explicitamente_nomeados(*, x=7, y=7):
    """x e y devem ser chamados de maneira nomiada

    Na falta de x ou y o valor 7 será usado
    """
    print(f'x: {x}, y: {y}')
    return x + y

def soma_explicitamente_nomeados2(x=7, *,  y=7):
    """x pode ser posicional ou não mas necessariamente y precisa ser nominal.

    Na falta de x ou y o valor 7 será usado
    """
    print(f'x: {x}, y: {y}')
    return x + y

def soma_explicitamente_posicionais(x, y, /):
    """x e y somente posicional.

    Na falta de x ou y o valor 7 será usado
    """
    print(f'x: {x}, y: {y}')
    return x + y

def soma_tudo_mix(x, y, /, z, *, w):
    """ x e y como estritamente posicionais, z como misto e w como estritamente nomiado."""

    return sum((x, y, z, w))


