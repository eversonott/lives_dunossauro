from contextlib import contextmanager
from datetime import datetime
from os import makedirs
from os.path import exists
from shutil import copyfileobj, rmtree
from requests import get

path = 'download'
if exists(path):
    rmtree(path)
makedirs(path)

def get_sprite_url(url, sprite='front_default'):
    """Pega a url do sprite."""
    return url['name'], get(url['url']).json()['sprites'][sprite]


def get_bin_file(args):
    """Faz o download do binário."""
    name, url = args
    return name, get(url, stream=True).raw


def save_file(args, path=path, type = 'png'):
    """Salva o binário no disco como imagem."""
    name, binary = args
    fname = f'{path}/{name}.{type}'
    with open(fname, 'wb') as f:
        copyfileobj(binary, f)
    return fname

def pipeline(*funcs):
    def inner(argument):
        state = argument
        for func in funcs:
            state = func(state)
    return inner

target = pipeline(get_sprite_url, get_bin_file, save_file)

@contextmanager
def timeit(*args):
    start_time = datetime.now()
    yield
    time_elapsed = datetime.now() - start_time
    print(f'Tempo total (hh:mm:ss.ms) {time_elapsed}')
