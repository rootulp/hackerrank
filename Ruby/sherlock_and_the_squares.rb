t = gets.to_i
t.times{
  (a, b) = gets.split.map{|i| i.to_i}
  small_a = ((a-1)**0.5).floor
  small_b = (b**0.5).floor
  puts small_b - small_a
}