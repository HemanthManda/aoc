from typing import List


def read_input(path: str):
    f = open(path, 'r+')
    lines = [line.strip('\n') for line in f]
    f.close()
    return lines
