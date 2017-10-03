def solve(x)
  if x.even?
    puts (x / 2)**2
  else
    puts ((x - 1) / 2)**2 + (x - 1) / 2
  end
end

n = gets.to_i
test_arr = []
n.times { test_arr << gets.to_i }
test_arr.each { |x| solve(x) }
