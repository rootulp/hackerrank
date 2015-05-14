def solve(combinations)
  combinations.each do |combination|
    return "YES" if combination[0].gcd(combination[1]) == 1
  end
  return "NO"
end

t = gets.to_i
t.times do 
    n = gets.to_i
    nums = gets.split(" ").map {|x| x.to_i}
    combinations = nums.combination(2).to_a
    puts solve(combinations)
end