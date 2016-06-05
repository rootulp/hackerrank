t = gets.to_i
t.times do
  (length, width) = gets.split(' ').map(&:to_i)
  side = length.gcd(width)
  puts length * width / (side**2)
end
