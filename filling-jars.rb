(size, operations) = gets.split.map{|i| i.to_i}
jars = Array.new(size, 0)
operations.times do
    (start, stop, value) = gets.split.map{|i| i.to_i}
    jars.each_index do |i|
        if i >= start-1 and i <= stop-1
            jars[i] = jars[i] + value
        end
    end
end
puts jars.inject{ |sum, element| sum + element }.to_i / jars.size