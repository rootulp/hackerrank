_ = gets.chomp
clouds = gets.chomp.split(' ').map(&:to_i)

current_cloud = 0
target_cloud = clouds.size - 1
jumps = 0
until current_cloud == target_cloud
  current_cloud += clouds[current_cloud + 2].zero? ? 2 : 1
  jumps += 1
end
puts jumps
