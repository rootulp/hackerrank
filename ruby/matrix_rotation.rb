class MatrixRotation

  attr_accessor :matrix
  def initialize
    @matrix = []
  end

  # def rotate(num_rotations)
  #   num_rotations.times { rotate }
  # end

  def rotate
    top = 0
    left = 0
    bot = matrix.size - 1
    right = matrix[0].size - 1
    rotate_layer(top, bot, left, right)
  end

  def rotate_layer(top, bot, left, right)
    p "top: #{top} bot: #{bot} left: #{left} right: #{right}"

    y1 = top
    x1 = left
    y2 = top
    x2 = left + 1

    until (y2 == top && x2 == left)
      swap(x1, y1, x2, y2)
      x1 = x2
      y1 = y2

      if (y2 == top && x2 == right)
        y2 += 1
      elsif (y2 == bot && x2 == right)
        x2 -= 1
      elsif (y2 == bot && x2 == left)
        y2 -= 1
      elsif (y2 == top)
        x2 += 1
      elsif (x2 == right)
        y2 += 1
      elsif (y2 == bot)
        x2 -= 1
      elsif (x2 == left)
        y2 -= 1
      end
      p "x2: #{x2} y2: #{y2}"
    end

  end

  def swap(x1, y1, x2, y2)
    matrix[y1][x1], matrix[y2][x2]= matrix[y2][x2], matrix[y1][x1]
  end

end

test = MatrixRotation.new

m, _, r = gets.split(" ").map(&:to_i)
m.times do
  test.matrix << (gets.split(" ").map(&:to_i))
end

p test.matrix
test.rotate
p test.matrix
# test.rotate(r)

