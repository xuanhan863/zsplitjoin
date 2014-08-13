#!/usr/bin/env python
import sys
from unipath import Path
from zsplitjoin import split_file

def main():
    split_file(Path(sys.argv[1]), number_of_files=int(sys.argv[2]))


if __name__ == '__main__':
    main()