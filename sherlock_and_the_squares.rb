def squares_between(a, b)
  perfect_squares = []
  for i in a..b
    perfect_squares << i if is_square?(i)
  end
  return perfect_squares.size
end

def is_square?(x)
  return true if x**0.5 % 1 == 0
  false
end

t = gets.to_i
t.times{
  (a, b) = gets.split.map{|i| i.to_i}
  puts squares_between(a,b)
}
