def possible?(radius_squared, stations)
    cities_needed = 0
    radius = radius_squared **0.5.ceil
    for x in -radius..radius
        for y in -radius..radius
            if x**2 + y**2 == radius_squared
                cities_needed += 1
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