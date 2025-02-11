class SantaGrid:
    def __init__(self):
        self._visited = set()

    def add_visit(self, x, y):
        self._visited.add(f'{x},{y}')

    def unique_visits(self):
        return len(self._visited)


class SantaTracker:
    def __init__(self, grid: SantaGrid | None = None):
        self._grid = grid or SantaGrid()
        self._x = 0
        self._y = 0
        self._grid.add_visit(self._x, self._y)

    def move(self, direction: str):
        if direction == '^':
            self._y += 1
        elif direction == 'v':
            self._y -= 1
        elif direction == '>':
            self._x += 1
        elif direction == '<':
            self._x -= 1
        else:
            raise Exception(f'Unknown direction {direction}')

        self._grid.add_visit(self._x, self._y)

    def presents_delivered(self):
        return self._grid.unique_visits()

