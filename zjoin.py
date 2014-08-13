#!/usr/bin/env python
import sys
from zsplitjoin import join_file


def main():
    join_file(sys.argv[1], exit_file_name=sys.argv[2])


if __name__ == '__main__':
    main()
