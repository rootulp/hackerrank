class InsertionSort
  attr_accessor :nums, :num_moves
  def initialize(nums)
    @nums = nums
    @num_moves = 0
    sort(nums)
  end

  def sort(nums)
    (1..nums.size - 1).each do |i|
      while i > 0 && nums[i - 1] > nums[i]
        swap(i, i - 1)
        i -= 1
      end
    end
  end

  def swap(a, b)
    nums[a], nums[b] = nums[b], nums[a]
    @num_moves += 1
  end
end

t = gets.to_i
t.times do
  _ = gets
  nums = gets.split(' ').map(&:to_i)
  puts InsertionSort.new(nums).num_moves
end
