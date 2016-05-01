(size, operations) = gets.split.map(&:to_i)
total = 0
operations.times do
  (start, stop, value) = gets.split.map(&:to_i)
  num = stop - start + 1
  total += num * value
end
puts total / size
