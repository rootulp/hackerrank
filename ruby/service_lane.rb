def max_width(entry, exit, highway)
  subarray = highway[entry..exit]
  puts subarray.min
end

(_, t) = gets.split.map(&:to_i)
highway = gets.split.map(&:to_i)
t.times do
  (entry, exit) = gets.split.map(&:to_i)
  max_width(entry, exit, highway)
end
