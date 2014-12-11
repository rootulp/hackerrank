num_packets = gets.to_i
kids = gets.to_i
packets = []
num_packets.times do
  packets << gets.to_i
end

packets.sort_by! { |i| i }
ans = packets[-1]

for i in 0..(num_packets - kids) do
  min = packets[i]
  max = packets[(i + kids - 1)]
  unfairness = max - min
  ans = unfairness if unfairness < ans
end

puts ans