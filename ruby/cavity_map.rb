# Cavity Map
class CavityMap
  attr_accessor :dimensions, :grid
  def initialize(dimensions)
    @dimensions = dimensions
    @grid = []
  end

  def cavity_map
    result = ''
    grid.each_with_index do |r, row|
      r.each_with_index do |_, col|
        result += cavity_helper(row, col)
      end
      result += "\n"
    end
    result
  end

  def cavity_helper(row, col)
    cavity?(row, col) ? 'X' : grid[row][col].to_s
  end

  def cavity?(row, col)
    return false if edge?(row, col)
    neighbors(row, col).each do |neighbor|
      return false if grid[row][col] <= neighbor
    end
    true
  end

  def edge?(row, col)
    row == 0 || row == dimensions - 1 || col == 0 || col == dimensions - 1
  end

  def neighbors(row, col)
    [grid[row][col + 1],
     grid[row][col - 1],
     grid[row + 1][col],
     grid[row - 1][col]]
  end
end

n = gets.to_i
test_case = CavityMap.new(n)
n.times do
  test_case.grid << gets.chomp.split(//).map(&:to_i)
end
puts test_case.cavity_map
