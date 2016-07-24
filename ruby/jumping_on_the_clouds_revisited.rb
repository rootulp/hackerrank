n, k = gets.chomp.split(' ').map(&:to_i)
clouds = gets.chomp.split(' ').map(&:to_i)

energy = 100
current_cloud = k % n
energy -= clouds[current_cloud] == 0 ? 1 : 3

until current_cloud == 0
  current_cloud = (current_cloud + k) % n
  energy -= clouds[current_cloud] == 0 ? 1 : 3
end

puts energy
