import os
import sys

from .wrapping import calculate_all_wrapping_feet, calculate_all_ribbon


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception('Filename must be supplied')

    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise Exception("Can not read the file")

    with open(filename, 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    print(calculate_all_wrapping_feet(lines))
    print(calculate_all_ribbon(lines))
