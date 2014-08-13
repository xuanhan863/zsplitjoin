#!/usr/bin/env python
import sys
from unipath import Path
from zsplitjoin import join_file

def main():
    join_file(Path(sys.argv[1]), exit_file_name=sys.argv[2])

if __name__ == '__main__':
    main()