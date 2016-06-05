# Plus Minus
class PlusMinus
  attr_reader :nums
  def initialize(nums)
    @nums = nums
  end

  def print_ratios
    puts ratio(count_positive), ratio(count_negative), ratio(count_zero)
  end

  private

  def ratio(numerator)
    numerator / nums.size.to_f
  end

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
nums = gets.chomp.split(' ').map(&:to_i)
PlusMinus.new(nums).print_ratios
