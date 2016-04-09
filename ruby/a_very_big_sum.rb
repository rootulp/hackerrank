_ = gets.to_i
puts gets.split(' ').map(&:to_i).reduce(:+)
