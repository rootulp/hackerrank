t = gets.to_i
t.times do
  (a, b, x) = gets.split(' ').map(&:to_i)
  num_to_find = a**b
  high = x

  while high < num_to_find
    low = high
    high += x
  end

  diff_low = (num_to_find - low).abs
  diff_high = (high - num_to_find).abs

  puts diff_low < diff_high ? low : high
end
