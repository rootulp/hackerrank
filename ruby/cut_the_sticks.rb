_ = gets.to_i
sticks = gets.chomp.split(" ").map { |stick| stick.to_i }

def main(sticks)
  if !sticks.empty?
    puts sticks.length
    cut_size = sticks.min
    sticks.map! { |stick| stick - cut_size }
    sticks.delete(0)
    main(sticks)
  end
end

main(sticks)
