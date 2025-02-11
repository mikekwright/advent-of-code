import os
import sys

from .mapping import SantaTracker, SantaGrid


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise Exception('Filename must be supplied')

    filename = sys.argv[1]
    if not os.path.exists(filename):
        raise Exception("Can not read the file")

    with open(filename, 'r') as f:
        input = f.read().strip()

    model = SantaTracker()
    for direction in input:
        model.move(direction)

    print(model.presents_delivered())

    shared_grid = SantaGrid()
    santa = SantaTracker(grid=shared_grid)
    robo = SantaTracker(grid=shared_grid)

    user_is_santa = True
    for direction in input:
        if user_is_santa:
            santa.move(direction)
        else:
            robo.move(direction)
        user_is_santa = not user_is_santa

    print(shared_grid.unique_visits())
