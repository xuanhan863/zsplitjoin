# coding: utf-8
from math import ceil
from unipath import Path
from .utils import get_real_size, read_in_chunks


def split_file(path, number_of_files, splitted_file_size, output_file_name, chunk_size, no_increase):
    path = Path(path)
    if not splitted_file_size is None:
        splitted_file_size = get_real_size(splitted_file_size)
    chunk_size = get_real_size(chunk_size)
    origin_file_size = path.size()
    if splitted_file_size and number_of_files is None:
        if no_increase:
            number_of_files = int(origin_file_size / splitted_file_size)
        else:
            number_of_files = ceil(float(origin_file_size) / splitted_file_size)
    else:
        if number_of_files is None:
            number_of_files = 5
        splitted_file_size = origin_file_size / number_of_files

    if output_file_name is None:
        output_file_name = path.name

    new_files_name = '{output_file_name}.part%d'.format(output_file_name=output_file_name)
    new_files = [new_files_name % i for i in range(1, int(number_of_files)+1)]

    with open(path, 'rb') as origin_file:
        file_iter = read_in_chunks(origin_file, chunk_size)
        for cur_file_name in new_files:
            is_last = cur_file_name == new_files[-1]
            cur_file_path = Path(cur_file_name)
            cur_file_size = 0
            with open(cur_file_path, 'wb') as cur_writing_file:
                while (cur_file_size < splitted_file_size if not is_last else True):
                    try:
                        piece = next(file_iter)
                    except StopIteration:
                        break
                    cur_writing_file.write(piece)
                    cur_file_size += chunk_size
