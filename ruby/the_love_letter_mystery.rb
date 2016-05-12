def analyze(test_arr, num_reductions)
  return num_reductions if test_arr.length <= 1
  x = test_arr.pop
  y = test_arr.shift
  num_reductions += num_reductions_for_pair(x, y, 0)
  analyze(test_arr, num_reductions)
end

def num_reductions_for_pair(x, y, counter)
  comparison = x <=> y
  if comparison == 1
    num_reductions_for_pair((x.ord - 1).chr, y, counter + 1)
  elsif comparison == -1
    num_reductions_for_pair(x, (y.ord - 1).chr, counter + 1)
  else
    counter
  end
end

gets.to_i.times do
  puts analyze(gets.chomp.chars, 0)
end
