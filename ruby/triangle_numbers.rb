num_tests = gets.to_i

num_tests.times do
    n = gets.to_i

    if n % 2 != 0
        puts "2"
    elsif ((n / 2) % 2) == 0
        puts "3"
    else
        puts "4"
    end

end
