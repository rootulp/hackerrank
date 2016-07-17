gets.chomp.to_i.times do
  n, m, s = gets.chomp.split(' ').map(&:to_i)
  dead_prisoner = (s + m - 1) % n
  puts dead_prisoner == 0 ? n : dead_prisoner
end
