/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */
function add(a, b) {
  return a + b;
}

class Polygon {
  constructor(side_lengths) {
    this.side_lengths = side_lengths;
  }

  perimeter() {
    return this.side_lengths.reduce(add, 0);
  }
}
