import os
import sys

from .santa_miner import find_the_santa_mine

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception('Filename must be supplied')

    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise Exception("Can not read the file")

    with open(filename, 'r') as f:
        input = f.read().strip()

    print(find_the_santa_mine(input))
    print(find_the_santa_mine(input, count=6))
