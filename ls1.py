#!/usr/bin/env python3

""" this little script prints size of all subdirectories and files 1-level deep relative to given path

    usage:  python ls1.py [-S] [-r] <path>
"""

import os
import argparse
import operator
import pathlib


def humanize_bytes(bytes, precision=1):
    """Return a humanized string representation of a number of bytes.
    >>> humanize_bytes(1024*12342)
    '12.1 MB'
    """

    abbrevs = (
        (1<<50, 'PB'),
        (1<<40, 'TB'),
        (1<<30, 'GB'),
        (1<<20, 'MB'),
        (1<<10, 'kB'),
        (1, 'b')
    )
    if bytes == 1:
        return '1b'
    for factor, suffix in abbrevs:
        if bytes >= factor:
            break
    return '%.*f%s' % (precision, bytes / factor, suffix)


def get_dir_size(path):
    dirSize = 0
    for dirName, subdirList, fileList in os.walk(path):
        try:
            dirSize += sum(os.path.getsize(os.path.join(dirName, name)) for name in fileList)
        except OSError:
            pass
    return dirSize


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to the directory")
    parser.add_argument("-S", help="sort by file size, smallest first", action="store_true")
    parser.add_argument("-r", "--reverse", help="reverse order while sorting", action="store_true")
    args = parser.parse_args()

    path = pathlib.Path(args.path).resolve()
    file_sizes = []

    for f in os.listdir(path):
        fullpath = os.path.join(path, f)
        if os.path.isfile(fullpath):
            file_sizes.append(('f', os.path.getsize(fullpath), f))
        elif os.path.isdir(fullpath):
            file_sizes.append(('d', get_dir_size(fullpath), f))
        else:
            print("%s %s" % (f, 'not a file or directory'))


    if args.S:
        file_sizes.sort(key = operator.itemgetter(1), reverse = args.reverse)
    for type, size_bytes, filename in file_sizes:
        print("%s %9s %s" % (type, humanize_bytes(size_bytes), filename))
