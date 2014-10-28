def create_possible_solutions(curr_num, solution_length, possible_solutions)
    if curr_num.length == solution_length
        possible_solutions << curr_num
    else
        create_possible_solutions(curr_num + "3", solution_length, possible_solutions)
        create_possible_solutions(curr_num + "5", solution_length, possible_solutions)
    end
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
    possible_solutions = []
    create_possible_solutions("", solution_length, possible_solutions)
    solutions = test_possible_solutions(possible_solutions)
    print_solution(solutions)
}