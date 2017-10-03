class MatrixRotation
  attr_accessor :matrix
  def initialize
    @matrix = []
  end

  def pretty_print
    puts matrix.map { |row| row.join(' ') }
  end

  def rotate(rotations)
    layers.each do |layer|
      (rotations % elements_in_layer(layer)).times { rotate_layer(*layer) }
    end
  end

  private

  def layers
    layers = []

    top = 0
    left = 0
    bot = matrix.size - 1
    right = matrix[0].size - 1

    while top < bot && left < right
      layers << [top, bot, left, right]
      top += 1; left += 1; bot -= 1; right -= 1
    end

    layers
  end

  def elements_in_layer(layer)
    top, bot, left, right = layer
    (2 * (bot - top)) + (2 * (right - left))
  end

  def rotate_layer(top, bot, left, right)
    y1 = top
    x1 = left
    y2 = top
    x2 = left + 1

    until y2 == top && x2 == left
      swap(x1, y1, x2, y2)
      x1 = x2
      y1 = y2

      if y2 == top && x2 == right
        y2 += 1
      elsif y2 == bot && x2 == right
        x2 -= 1
      elsif y2 == bot && x2 == left
        y2 -= 1
      elsif y2 == top
        x2 += 1
      elsif x2 == right
        y2 += 1
      elsif y2 == bot
        x2 -= 1
      elsif x2 == left
        y2 -= 1
      end
    end
  end

  def swap(x1, y1, x2, y2)
    matrix[y1][x1], matrix[y2][x2] = matrix[y2][x2], matrix[y1][x1]
  end
end

test_case = MatrixRotation.new
m, _, rotations = gets.split(' ').map(&:to_i)
m.times { test_case.matrix << gets.split(' ').map(&:to_i) }
test_case.rotate(rotations)
test_case.pretty_print
