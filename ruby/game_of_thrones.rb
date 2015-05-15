odds = 0
chars = gets.chomp.split(//).sort
uniq_chars = chars.uniq

def is_odd?(num)
  return true if num % 2 == 1
  false
end

uniq_chars.each do |curr_char|
  char_occurences = chars.count(curr_char).to_i
  if is_odd?(char_occurences)
    odds += 1
  end
end

if odds <= 1
  puts "YES"
else
  puts "NO"
end
