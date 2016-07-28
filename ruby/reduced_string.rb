def reduce_string(str)
  reduce(str) until reduced?(str)
  str.empty? ? 'Empty String' : str
end

def reduce(str)
  str.sub!(adjacent_pairs(str).first.join, '')
end

def reduced?(str)
  adjacent_pairs(str).empty?
end

def adjacent_pairs(str)
  str.chars.each_cons(2).select { |c1, c2| c1 == c2 }
end

str = gets.chomp
puts reduce_string(str)
