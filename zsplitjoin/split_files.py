# coding: utf-8
from .utils import read_in_chunks
from unipath import Path


def split_file(path, number_of_files=2, new_file_size=None, exit_file_name=None, chunk_size=1024):
    path = Path(path)
    if number_of_files is None:
        number_of_files = path.size() / new_file_size
    else:
        new_file_size = path.size() / number_of_files

    if exit_file_name is None:
        exit_file_name = path.name

    new_files_name = '{exit_file_name}.part%d'.format(exit_file_name=exit_file_name)
    new_files = [new_files_name % i for i in range(1, number_of_files+1)]

    with open(path, 'rb') as origin_file:
        file_iter = read_in_chunks(origin_file, chunk_size)
        for cur_file_name in new_files:
            cur_file_path = Path(cur_file_name)
            cur_file_size = 0
            with open(cur_file_path, 'wb') as cur_writing_file:
                while cur_file_size < new_file_size:
                    try:
                        piece = next(file_iter)
                    except StopIteration:
                        break
                    cur_writing_file.write(piece)
                    cur_file_size += chunk_size
