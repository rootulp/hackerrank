def solve(flavors, money)
    flavors.each_with_index do |flavor, index|    
        if flavors.include?(money - flavor)
            a = index + 1
            b = flavors.index(money - flavor) + 1
            if b == a
                b = flavors.rindex(money - flavor) + 1
            end
            return a.to_s + " " + b.to_s
        end
    end
end

t = gets.to_i
t.times {
    money = gets.to_i
    num_flavors = gets.to_i
    flavors = gets.split.map{|x| x.to_i}
    puts solve(flavors, money)
}