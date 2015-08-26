def factorial(n)
  n == 1 ? 1 : n * factorial(n - 1)
end

puts factorial(gets.to_i)
