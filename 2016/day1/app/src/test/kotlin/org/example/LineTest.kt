package org.example

import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertNull

class LineTest {
  @Test fun `Parallel lines do not cross`() {
    val leftLine = Line(Point(0, 0), Point(5, 0))
    val rightLine = Line(Point(1, 2), Point(10, 2))

    assertNull(leftLine.overlaps(rightLine))
  }

  @Test fun `Lines that are perpendicular but don't overlap should not cross`() {
    val leftLine = Line(Point(0, 0), Point(5, 0))
    val rightLine = Line(Point(10, 5), Point(10, -5))

    assertNull(leftLine.overlaps(rightLine))
  }

  @Test fun `Lines perpendicular should return the point where they intercept`() {
    val expectedIntersect = Point(1, 1)

    val leftLine = Line(Point(-3, 1), Point(3, 1))
    val rightLine = Line(Point(1, 5), Point(1, -5))

    val actualIntersect = leftLine.overlaps(rightLine)
    
    assertEquals(expectedIntersect, actualIntersect)
  }

  @Test fun `Lines perpendicular with overlap on edge should return where they intercept`() {
    val expectedIntersect = Point(0, 3)

    val leftLine = Line(Point(0, 3), Point(5, 3))
    val rightLine = Line(Point(0, 5), Point(0, -2))

    val actualIntersect = leftLine.overlaps(rightLine)
    
    assertEquals(expectedIntersect, actualIntersect)
  }
}
