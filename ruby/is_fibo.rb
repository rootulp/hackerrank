fib_nums = [0, 1]
fib_nums << fib_nums[-1] + fib_nums[-2] while fib_nums[-1] < 10**10
n = gets.chomp.to_i
n.times do
  t = gets.chomp.to_i
  if fib_nums.include?(t)
    puts 'IsFibo'
  else
    puts 'IsNotFibo'
  end
end
