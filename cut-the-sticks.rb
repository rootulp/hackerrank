num_sticks = gets.to_i
sticks = gets.chomp.split(" ").map {|stick| stick.to_i}

def main(sticks)
    if !sticks.empty?
        puts sticks.length
        cut_size = sticks.min
        sticks.map! do |stick|
            stick - cut_size
        end
        sticks.delete(0)
        main(sticks)
    end
end

main(sticks)