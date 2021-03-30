"""
0:06:57.100544
Primeira etapa do problema:
    - Fazer download das imagens dos 100 primeiros pokemons da pokeapi
    """
from datetime import datetime
from os import makedirs
from requests import get
from os.path import exists
from shutil import rmtree, copyfileobj
from urllib.parse import urljoin
from pprint import pprint


path = 'download'
base_url = 'https://pokeapi.co/api/v2/'

if exists(path):
    rmtree(path)
makedirs(path)


def download_file(name, url, *, path=path, type = 'png'):
    """ Faz o download de um arquivo. """
    response = get(url, stream=True)
    fname = f'{path}/{name}.{type}'
    with open(fname, 'wb') as f:
        copyfileobj(response.raw, f)
        return fname


def get_sprite_url(url, sprite='front_default'):
    return get(url).json()['sprites'][sprite]

start_time = datetime.now()

pokemons = get(urljoin(base_url,'pokemon/?limit=100')).json()['results']

images_url = {j['name']: get_sprite_url(j['url']) for j in pokemons}

files = [download_file(name, url) for name, url in images_url.items()]

time_elapsed = datetime.now() - start_time

print(f'Tempo total (hh:mm:ss.msresults) {time_elapsed}')

pprint(files)
