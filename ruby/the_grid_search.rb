# Grid Search
class GridSearch
  attr_accessor :grid, :pattern_grid
  def initialize
    @grid = []
    @pattern_grid = []
  end

  def contains_pattern
    search_grid ? 'YES' : 'NO'
  end

  private

  def search_grid
    0.upto(grid.size - 1) do |y|
      0.upto(grid[0].size - 1) do |x|
        return true if valid_grid(y, x)
      end
    end

    false
  end

  def valid_grid(y, x)
    pattern_grid.each_with_index do |pattern_row, pattern_y|
      pattern_row.each_with_index do |pattern_element, pattern_x|
        return false if pattern_element != grid[y + pattern_y][x + pattern_x]
      end
    end
    true
  end
end

t = gets.to_i
t.times do
  g = GridSearch.new
  r, = gets.split(' ').map(&:to_i)
  r.times { g.grid << gets.chomp.split(//) }
  r, = gets.split(' ').map(&:to_i)
  r.times { g.pattern_grid << gets.chomp.split(//) }
  puts g.contains_pattern
end
