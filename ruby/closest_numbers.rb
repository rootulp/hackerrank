_ = gets.chomp
nums = gets.split().map {|x| x.to_i}.sort!

min_dif = nums.max
closest = []
nums.each_with_index do |num, index|
    if index != 0
        if num - nums[index-1] == min_dif
            closest << nums[index-1]
            closest << num
        elsif num - nums[index-1] < min_dif
            min_dif = num - nums[index-1]
            closest = [num, nums[index-1]]
        end
    end
end

puts closest.sort!.join(" ")
