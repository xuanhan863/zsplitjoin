# coding: utf-8
from unipath import Path
from .utils import create_file_name, files_iter, get_real_size, read_in_chunks


def join_file(path, output_file_name=None, chunk_size='1K'):
    path = Path(path)
    chunk_size = get_real_size(chunk_size)
    if output_file_name is None:
        output_file_path = create_file_name(path)
    else:
        output_file_path = Path(output_file_name)

    output_file_path.write_file(b'', 'wb')

    with open(output_file_path, 'wb') as output_file:
        for cur_file_name in files_iter(path):
            with open(cur_file_name, 'rb') as cur_file:
                for piece in read_in_chunks(cur_file, chunk_size):
                    output_file.write(piece)
