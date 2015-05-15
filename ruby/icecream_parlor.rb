def solve(flavors, money)
    pairs = flavors.combination(2)
    pairs.each do |pair|
        if pair[0] + pair[1] == money
            a = flavors.index(pair[0]) + 1
            b = flavors.rindex(pair[1]) + 1
            return a.to_s + " " + b.to_s
        end
    end
end

t = gets.to_i
t.times {
    money = gets.to_i
    _ = gets.to_i
    flavors = gets.split.map{|x| x.to_i}
    puts solve(flavors, money)
}
