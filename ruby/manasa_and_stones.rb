def last_stone(stones, a, b)
  puts all_stones(stones, a, b).uniq.sort.join(' ')
end

def all_stones(stones, a, b)
  results = []
  (0..stones).each do |i|
    results << (i * a) + ((stones - i) * b)
    results << (i * b) + ((stones - i) * a)
  end
  results
end

t = gets.to_i
t.times do
  stones = gets.to_i
  a = gets.to_i
  b = gets.to_i
  last_stone(stones - 1, a, b)
end
