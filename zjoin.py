#!/usr/bin/env python
import sys
from optparse import OptionParser
from zsplitjoin import join_file


def main():
    usage = 'Usage: zjoin.py [options] [file]\n the file must have the extension .part1'
    opar = OptionParser(usage=usage)
    opar.add_option("-o", "--output", dest="output",
                    help="output file name", type="str", default=None)
    opar.add_option("-c", "--chunk", dest="chunk",
                    help="chunk size", type="str", default='1K')

    options, args = opar.parse_args(sys.argv)
    if len(args) <= 1:
        print('invalid input')
        sys.exit(0)

    join_file(args[1], output_file_name=options.output, chunk_size=options.chunk)


if __name__ == '__main__':
    main()
