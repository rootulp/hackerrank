def possible?(radius_squared, stations)
    cities_needed = 4
    radius = (radius_squared ** 0.5).to_i
    for x in 1..(radius-1)
        for y in 1..(radius-1)
            if x**2 + y**2 == radius_squared
                cities_needed += 4
            end
        end
    end
    return true if stations >= cities_needed
    false
end

t = gets.to_i
t.times do
    (radius_squared, stations) = gets.split(" ").map{|x| x.to_i}
    if possible?(radius_squared, stations)
        puts "possible"
    else
        puts "impossible"
    end
end
