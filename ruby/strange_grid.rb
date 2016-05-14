# Strange Grid
class StrangeGrid
  def self.val_at(row, col)
    suffix = col * 2 - 1
    suffix -= 1 if row.odd?
    prefix = (row - 1) / 2
    "#{prefix}#{suffix}".to_i
  end
end

row, col = gets.split(' ').map(&:to_i)
puts StrangeGrid.val_at(row, col)
