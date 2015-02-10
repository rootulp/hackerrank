class CavityMap
  attr_accessor :n, :grid
  def initialize(n)
    @n = n
    @grid = []
  end

  def cavity_map
    result = ""
    grid.each_with_index do |r, row|
      r.each_with_index do |val, col|
        if cavity?(row, col)
          result += "X"
        else
          result += grid[row][col].to_s
        end
      end
      result += "\n"
    end
    result
  end

  def cavity?(row, col)
    return false if edge?(row, col)
    neighbors(row, col).each do |neighbor|
      return false if grid[row][col] <= neighbor
    end
    true
  end

  def edge?(row, col)
    row == 0 || row == n-1 || col == 0 || col == n-1 ? true : false
  end

  def neighbors(row, col)
    [grid[row][col+1],
     grid[row][col-1],
     grid[row+1][col],
     grid[row-1][col]] 
  end

end

n = gets.to_i
test_case = CavityMap.new(n)
n.times do
  test_case.grid << gets.chomp.split(//).map{|x| x.to_i}
end
puts test_case.cavity_map
#p test_case.cavity?(0, 1)