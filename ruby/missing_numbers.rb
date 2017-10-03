occurences = Hash.new(0)

_ = gets.to_i
list_a = gets.split(' ').map(&:to_i)
_ = gets.to_i
list_b = gets.split(' ').map(&:to_i)

list_b.each { |num| occurences[num] += 1 }
list_a.each { |num| occurences[num] -= 1 }
occurences.keep_if { |_num, count| count > 0 }

puts occurences.keys.sort.join(' ')
