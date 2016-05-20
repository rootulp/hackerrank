require 'prime'

# Smith Number
class SmithNumber
  def self.valid?(num)
    sum_of_factors(num) == sum_of_digits(num) ? 1 : 0
  end

  def self.sum_of_factors(num)
    Prime.prime_division(num).map do |factor|
      sum_of_digits(factor.first) * factor.last
    end.reduce(:+)
  end

  def self.sum_of_digits(num)
    num.to_s.chars.map(&:to_i).reduce(:+)
  end
end

puts SmithNumber.valid?(gets.to_i)
