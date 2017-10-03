def partition(ar)
  p = ar.shift
  a = []
  b = []
  ar.each do |val|
    a << val if val < p
    b << val if val >= p
  end
  result = a << p << b
  result.join(' ')
end

_ = gets.to_i
ar = gets.chomp.split.map(&:to_i)
puts partition(ar)
