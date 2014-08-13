# coding: utf-8

from unipath import Path


def read_in_chunks(file_object, chunk_size):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def files_iter(path):
    file_name = path.name.replace('.part1', '')
    file_name_base = '{file_name}.part%d'.format(file_name=file_name)
    i = 1
    while True:
        p = Path(file_name_base % i)
        if p.exists():
            yield p
        else:
            break
        i += 1


def create_file_name(path):
    exit_file_path = Path(path.name.replace('.part1', ''))
    exit_file_ext = exit_file_path.ext or '.dat'
    c = 0
    while exit_file_path.exists():
        aux = exit_file_path.name.replace(
            ' (%d)%s' % ((c-1), exit_file_ext),
            exit_file_ext
        ).replace(
            exit_file_ext,
            " (%d)%s" % (c, exit_file_ext)
        )
        exit_file_path = Path(aux)
        c += 1
    return exit_file_path