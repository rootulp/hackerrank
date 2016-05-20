t = gets.to_i
t.times { puts gets.chomp.split(' ').map(&:to_i).inject(:+) }
