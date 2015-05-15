def max_width(entry, exit, highway)
  subarray = highway[entry..exit]
  puts subarray.min
end

(_, t) = gets.split.map{|i| i.to_i}
highway = gets.split.map{|i| i.to_i}
t.times {
  (entry, exit) = gets.split.map{|i| i.to_i}
  max_width(entry, exit, highway)
}
