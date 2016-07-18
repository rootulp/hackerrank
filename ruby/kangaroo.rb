def same_square?(x1, v1, x2, v2)
  return true if x1 == x2
  return false if (x1 > x2 && v1 >= v2) || (x1 < x2 && v1 <= v2)
  same_square?(x1 + v1, v1, x2 + v2, v2)
end

x1, v1, x2, v2 = gets.strip.split(' ').map(&:to_i)
puts same_square?(x1, v1, x2, v2) ? 'YES' : 'NO'
