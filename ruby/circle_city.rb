def possible?(radius_squared, stations)
  cities_needed = 4
  radius = (radius_squared**0.5).to_i
  (1..(radius - 1)).each do |x|
    (1..(radius - 1)).each do |y|
      cities_needed += 4 if x**2 + y**2 == radius_squared
    end
  end
  stations >= cities_needed
end

t = gets.to_i
t.times do
  (radius_squared, stations) = gets.split(' ').map(&:to_i)
  puts possible?(radius_squared, stations) ? 'possible' : 'impossible'
end
