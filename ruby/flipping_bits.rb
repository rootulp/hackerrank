MASK = 4_294_967_295
num_cases = gets.to_i
num_cases.times do
  puts gets.to_i ^ MASK
end
