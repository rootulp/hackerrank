n = gets.to_i
k = gets.to_i
candy = Array.new(n)
for i in 0..n-1
      candy[i] = gets.to_i
end

candy.sort_by! { |i| i }
ans = candy[-1]

candy.each_cons(k) do |x|
  unfairness = x[-1] - x[0]
  ans = unfairness if unfairness < ans
end

puts ans