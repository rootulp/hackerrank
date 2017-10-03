def solve(solution_length)
  (0..solution_length).each do |x|
    possible_solution = '5' * (solution_length - x) + '3' * x
    return possible_solution if valid?(possible_solution)
  end
  '-1'
end

def valid?(curr_solution)
  num_3s = curr_solution.count('3')
  num_5s = curr_solution.count('5')
  return true if divisible_by(num_3s, 5) && divisible_by(num_5s, 3)
  false
end

def divisible_by(num, divisor)
  return true if (num % divisor).zero?
  false
end

t = gets.to_i
t.times do
  solution_length = gets.to_i
  puts solve(solution_length)
end
