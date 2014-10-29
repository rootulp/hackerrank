def create_possible_solutions(solution_length)
  possible_solutions = []
  for i in 0..solution_length do 
    possible_solutions << "5" * i + "3" * (solution_length - i)
  end
  return possible_solutions
end

def test_possible_solutions(possible_solutions)
  solutions = []
  possible_solutions.each do |curr_solution|
    solutions << curr_solution if is_valid?(curr_solution)
  end
  return solutions
end

def is_valid?(curr_solution)
  num_3s = curr_solution.count("3")
  num_5s = curr_solution.count("5")
  return true if divisible_by(num_3s, 5) && divisible_by(num_5s, 3)
  false
end

def divisible_by(num, divisor)
  return true if num % divisor == 0
  false
end

def print_solution(solutions)
  if solutions.empty?
    puts "-1"
  else
    puts solutions.max
  end
end

t = gets.to_i
t.times{
    solution_length = gets.to_i
    possible_solutions = create_possible_solutions(solution_length)
    solutions = test_possible_solutions(possible_solutions)
    print_solution(solutions)
}