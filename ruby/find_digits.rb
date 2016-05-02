t = gets.chomp.to_i
t.times do
  total = 0
  n = gets.chomp.to_i
  n.to_s.chars.map(&:to_i).each do |digit|
    next if digit == 0
    total += 1 if n % digit == 0
  end
  puts total
end
