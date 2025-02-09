package org.example

import kotlin.math.abs

data class Point(val x: Int, val y: Int) {
  fun distance(): Int {
    return abs(x) + abs(y)
  }
}
