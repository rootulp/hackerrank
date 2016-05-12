gets.to_i.times do
  n = gets.to_i
  if n.odd?
    puts '2'
  elsif (n / 2).even?
    puts '3'
  else
    puts '4'
  end
end
