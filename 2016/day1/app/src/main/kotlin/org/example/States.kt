package org.example

interface Direction {
  val point: Point
  fun move(dir: Char, distance: Int): Direction
}

class North(override val point: Point) : Direction {
  override fun move(dir: Char, distance: Int): Direction {
    if (dir.equals('R')) {
      return East(Point(point.x + distance, point.y))
    } else if (dir.equals('L')) {
      return West(Point(point.x - distance, point.y))
    }

    throw Exception("Unknown direction")
  }
}

class East(override val point: Point) : Direction {
  override fun move(dir: Char, distance: Int): Direction {
    if (dir.equals('R')) {
      return South(Point(point.x, point.y - distance))
    } else if (dir.equals('L')) {
      return North(Point(point.x, point.y + distance))
    }

    throw Exception("Unknown direction")
  }
}

class South(override val point: Point) : Direction {
  override fun move(dir: Char, distance: Int): Direction {
    if (dir.equals('R')) {
      return West(Point(point.x - distance, point.y))
    } else if (dir.equals('L')) {
      return East(Point(point.x + distance, point.y))
    }

    throw Exception("Unknown direction")
  }
}

class West(override val point: Point) : Direction {
  override fun move(dir: Char, distance: Int): Direction {
    if (dir.equals('R')) {
      return North(Point(point.x, point.y + distance))
    } else if (dir.equals('L')) {
      return South(Point(point.x, point.y - distance))
    }

    throw Exception("Unknown direction")
  }
}

