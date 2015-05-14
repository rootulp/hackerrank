t = gets.to_i
t.times {puts gets.chomp.split(" ").map{|x| x.to_i}.inject(:+)}
