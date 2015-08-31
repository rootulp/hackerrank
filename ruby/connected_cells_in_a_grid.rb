class ConnectedCells

  attr_accessor :matrix
  def initialize
    @matrix = []
  end

  def largest_region
    max = 1
    matrix.each_with_index do |row, y|
      row.each_with_index do |col, x|
        next if is_zero?(y, x)
        max = dfs([], y, x) if dfs([], y, x) > max
      end
    end
    max
  end

  private

  def dfs(visited, y, x)
    neighbors(y, x).each do |neighbor|
      y, x = neighbor
      next if visited.include?(neighbor) || is_zero?(y, x)
      visited << neighbor
      dfs(visited, y, x)
    end
    visited.size
  end

  def neighbors(y, x)
    neighbors = []
    [-1, 0, 1].product([-1, 0, 1]).map do |dy, dx|
      next if (dx == 0 && dy == 0) ||
              y + dy < 0 || y + dy >= matrix.size ||
              x + dx < 0 || x + dx >= matrix.first.size
      neighbors << [y + dy, x + dx]
    end
    neighbors
  end

  def is_zero?(y, x)
    matrix[y][x] == 0
  end
end

connected_cells = ConnectedCells.new
m = gets.to_i
_ = gets.to_i
m.times do
  connected_cells.matrix << gets.split(' ').map(&:to_i)
end
puts connected_cells.largest_region
