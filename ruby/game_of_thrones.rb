chars = gets.chomp.chars.sort
odds = 0

chars.uniq.each do |curr_char|
  odds += 1 if chars.count(curr_char).odd?
end

puts odds <= 1 ? 'YES' : 'NO'
