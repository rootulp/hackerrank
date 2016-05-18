# Taum
class Taum
  attr_reader :black_num, :white_num, :black_p, :white_p, :convert_p
  def initialize(black_num, white_num, black_p, white_p, convert_p)
    @black_num = black_num
    @white_num = white_num
    @black_p = black_p
    @white_p = white_p
    @convert_p = convert_p
  end

  def calc
    (black_num * black_price) + (white_num * white_price)
  end

  def black_price
    black_p > white_p + convert_p ? white_p + convert_p : black_p
  end

  def white_price
    white_p > black_p + convert_p ? black_p + convert_p : white_p
  end
end

t = gets.to_i
t.times do
  black_num, white_num = gets.split(' ').map(&:to_i)
  black_p, white_p, convert_p = gets.split(' ').map(&:to_i)
  puts Taum.new(black_num, white_num, black_p, white_p, convert_p).calc
end
