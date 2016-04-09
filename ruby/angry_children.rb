num_packets = gets.to_i
kids = gets.to_i
packets = []
num_packets.times { packets << gets.to_i }
packets.sort!
ans = packets[-1]

(0..(num_packets - kids)).each do |i|
  min = packets[i]
  max = packets[(i + kids - 1)]
  unfairness = max - min
  ans = unfairness if unfairness < ans
end

puts ans
