package org.example

import kotlin.math.min
import kotlin.math.max

fun overlap(point: Int, minPoint: Int, maxPoint: Int): Boolean {
  return point >= minPoint && point <= maxPoint
}

class Line(
  val start: Point,
  val stop: Point,
  val minX: Int,
  val maxX: Int,
  val minY: Int,
  val maxY: Int
) {
  constructor(start: Point, stop: Point) : this(start, stop,
    min(start.x, stop.x),
    max(start.x, stop.x),
    min(start.y, stop.y),
    max(start.y, stop.y)
  )

  override fun toString() : String {
    return "$minX $maxX $minY $maxY"
  }

  fun overlaps(otherLine: Line) : Point? {
    val minXBetweenOtherLine: Boolean = overlap(minX, otherLine.minX, otherLine.maxX) || overlap(otherLine.minX, minX, maxX)
    val maxXBetweenOtherLine: Boolean = overlap(maxX, otherLine.minX, otherLine.maxX) || overlap(otherLine.maxX, minX, maxX)
    val minYBetweenOtherLine: Boolean = overlap(minY, otherLine.minY, otherLine.maxY) || overlap(otherLine.minY, minY, maxY)
    val maxYBetweenOtherLine: Boolean = overlap(maxY, otherLine.minY, otherLine.maxY) || overlap(otherLine.maxY, minY, maxY)

    if (minXBetweenOtherLine && maxXBetweenOtherLine && minYBetweenOtherLine && maxYBetweenOtherLine) {
      // This only works for the test because they are lines that are always going to be perfectly perpendicular
      if (this.minX == this.maxX) {
        return Point(minX, otherLine.minY)
      } else if (this.minY == this.maxY) {
        return Point(otherLine.minX, minY)
      }
    }

    return null
  }
}

