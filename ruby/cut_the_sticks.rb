def cut_sticks(sticks)
  return if sticks.empty?
  puts sticks.length
  cut_size = sticks.min
  sticks.map! { |stick| stick - cut_size }
  sticks.delete(0)
  cut_sticks(sticks)
end

_ = gets.to_i
cut_sticks(gets.chomp.split(' ').map(&:to_i))
