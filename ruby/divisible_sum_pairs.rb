_, k = gets.chomp.split(' ').map(&:to_i)
arr = gets.chomp.split(' ').map(&:to_i)
puts arr.combination(2).count { |pair| pair.reduce(:+) % k == 0 }
