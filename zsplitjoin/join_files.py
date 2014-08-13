# coding: utf-8
from unipath import Path
from .utils import create_file_name, files_iter, read_in_chunks


def join_file(path, exit_file_name=None, chunk_size=1024):
    path = Path(path)
    if exit_file_name is None:
        exit_file_path = create_file_name(path)
    else:
        exit_file_path = Path(exit_file_name)

    exit_file_path.write_file('', 'wb')

    with open(exit_file_path, 'wb') as exit_file:
        for cur_file_name in files_iter(path):
            with open(cur_file_name, 'rb') as cur_file:
                for piece in read_in_chunks(cur_file, chunk_size):
                    exit_file.write(piece)
