# Connected Cells
class ConnectedCells
  attr_accessor :matrix
  def initialize
    @matrix = []
  end

  def largest_region
    max = 1
    matrix.each_with_index do |row, y|
      row.each_with_index do |_, x|
        next if zero?(y, x)
        max = dfs([], y, x) if dfs([], y, x) > max
      end
    end
    max
  end

  private

  def dfs(visited, y, x)
    neighbors(y, x).each do |neighbor|
      y, x = neighbor
      next if visited.include?(neighbor) || zero?(y, x)
      visited << neighbor
      dfs(visited, y, x)
    end
    visited.size
  end

  def neighbors(y, x)
    neighbors = []
    [-1, 0, 1].product([-1, 0, 1]).map do |dy, dx|
      next if invalid_neighbor(x, y, dx, dy)
      neighbors << [y + dy, x + dx]
    end
    neighbors
  end

  def zero?(y, x)
    matrix[y][x] == 0
  end

  def invalid_neighbor(x, y, dx, dy)
    (dx == 0 && dy == 0) ||
      y + dy < 0 || y + dy >= matrix.size ||
      x + dx < 0 || x + dx >= matrix.first.size
  end
end

connected_cells = ConnectedCells.new
m = gets.to_i
_ = gets.to_i
m.times { connected_cells.matrix << gets.split(' ').map(&:to_i) }
puts connected_cells.largest_region
