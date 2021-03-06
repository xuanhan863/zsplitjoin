# coding: utf-8
import re
from unipath import Path

try:
    unicode = unicode
except NameError:
    basestring = (str, bytes)


def read_in_chunks(file_object, chunk_size):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def files_iter(path):
    origin_file = path.name.replace('.part1', '')
    file_name_base = '{file_name}.part%d'.format(file_name=origin_file)
    i = 1
    while True:
        p = Path(file_name_base % i)
        if p.exists():
            yield p
        else:
            break
        i += 1


def create_file_name(path):
    output_file_path = Path(path.name.replace('.part1', ''))
    output_file_ext = output_file_path.ext or '.dat'
    c = 0
    while output_file_path.exists():
        aux = output_file_path.name.replace(
            ' (%d)%s' % ((c - 1), output_file_ext),
            output_file_ext
        ).replace(
            output_file_ext,
            " (%d)%s" % (c, output_file_ext)
        )
        output_file_path = Path(aux)
        c += 1
    return output_file_path


units = {
    'P': lambda x: x * (2**5) ** 10,
    'T': lambda x: x * (2**4) ** 10,
    'G': lambda x: x * (2**3) ** 10,
    'M': lambda x: x * (2**2) ** 10,
    'K': lambda x: x * (2**1) ** 10,
    'B': lambda x: x * (2**0) ** 10
}


def human_size_to_bytes(human_size):
    regex = re.compile("(?P<size>\d+)(?P<unit>[%s]{1})" % '|'.join(units))
    r = regex.search(human_size.upper())
    size, unit = r.groups()
    return units[unit](int(size) or 1)


def get_real_size(size):
    if isinstance(size, basestring):
        if not size.isdigit():
            size = human_size_to_bytes(size)
    return int(size)
