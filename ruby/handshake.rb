num_cases = gets.to_i
num_cases.times do
  ppl = gets.to_i
  puts ((ppl * (ppl - 1) / 2)).to_s
end
