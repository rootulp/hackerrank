class PlusMinus

  attr_reader :nums
  def initialize(nums)
    @nums = nums
  end

  def print_ratios
    puts count_positive / nums.size.to_f
    puts count_negative / nums.size.to_f
    puts count_zero     / nums.size.to_f
  end

  private

  def count_positive
    nums.count { |num| num > 0 }
  end

  def count_negative
    nums.count { |num| num < 0 }
  end

  def count_zero
    nums.count(0)
  end

end

_ = gets.chomp.to_i
nums = gets.chomp.split(" ").map(&:to_i)
PlusMinus.new(nums).print_ratios


