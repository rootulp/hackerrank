_ = gets.chomp.to_i
arr = gets.chomp.split(' ').map(&:to_i)
distances = arr.map.with_index { |curr, i| arr[i + 1..-1].index(curr) }.compact
puts distances.any? ? distances.min + 1 : -1
