t = gets.chomp.to_i
t.times do
    total = 0
    n = gets.chomp.to_i
    n_arr = n.to_s.split(//).map{|i| i.to_i}
    n_arr.each do |digit|
        if n % digit == 0
            total += 1
        end
    end
    puts total
end