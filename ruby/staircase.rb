# Staircase
class Staircase
  def self.draw(height)
    (1..height).each do |line_num|
      draw_line(line_num, height)
    end
  end

  def self.draw_line(line_num, height)
    (height - line_num).times { print(' ') }
    line_num.times { print('#') }
    print("\n")
  end
  private_class_method :draw_line
end

n = gets.chomp.to_i
Staircase.draw(n)
