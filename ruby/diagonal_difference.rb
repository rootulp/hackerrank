# Diagonal Difference
class DiagonalDifference
  attr_accessor :matrix
  def initialize
    @matrix = []
  end

  def add_row(row)
    matrix << row.split(' ').map(&:to_i)
  end

  def diagonal_difference
    (diagonal_one_elements.reduce(:+) - diagonal_two_elements.reduce(:+)).abs
  end

  private

  def diagonal_one_elements
    (0..(matrix.size - 1)).each_with_object([]) do |x, elements|
      elements << matrix[x][x]
    end
  end

  def diagonal_two_elements
    (0..(matrix.size - 1)).each_with_object([]) do |x, elements|
      elements << matrix[x][matrix.size - 1 - x]
    end
  end
end

test_case = DiagonalDifference.new
n = gets.to_i
n.times { test_case.add_row(gets.chomp) }
puts test_case.diagonal_difference
