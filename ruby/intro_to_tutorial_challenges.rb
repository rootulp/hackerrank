num_to_search = gets.to_i
_ = gets.to_i
num_array = gets.split.map{|x| x.to_i}

puts num_array.index(num_to_search)
