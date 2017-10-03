def solve(flavors, money)
  pairs = flavors.combination(2)
  pairs.each do |pair|
    next unless pair[0] + pair[1] == money
    a = flavors.index(pair[0]) + 1
    b = flavors.rindex(pair[1]) + 1
    return a.to_s + ' ' + b.to_s
  end
end

t = gets.to_i
t.times do
  money = gets.to_i
  _ = gets.to_i
  flavors = gets.split.map(&:to_i)
  puts solve(flavors, money)
end
