num_test_cases = gets.to_i
test_cases = []
num_test_cases.times { |_x| test_cases.push(gets.chomp) }
gem_stones = test_cases.shift.split(//).uniq

not_gem_stones = []
test_cases.each do |test_case|
  gem_stones.each do |curr_gem|
    not_gem_stones << curr_gem unless test_case.include?(curr_gem)
  end
end

gem_stones -= not_gem_stones
puts gem_stones.length
