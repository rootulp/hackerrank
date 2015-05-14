require 'prime'

class SmithNumber

  def self.valid?(num)
    sum_of_factors(num) == sum_of_digits(num) ? 1 : 0
  end

  def self.sum_of_factors(num)
    total = 0
    factors = Prime.prime_division(num)
    factors.each do |factor|
      if factor[0].to_s.length > 1
        total += sum_of_digits(factor[0])
      else
        total += factor[0] * factor[1]
      end
    end
    total
  end

  def self.sum_of_digits(num)
    total = 0
    num.to_s.chars.each do |digit|
      total += digit.to_i
    end
    total
  end
end

puts SmithNumber.valid?(gets.to_i)
