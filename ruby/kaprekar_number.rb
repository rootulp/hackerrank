# Kaprekar Number
class KaprekarNumber
  def self.find_all(min, max)
    solutions = (min..max).select { |num| valid?(num) }
    solutions.empty? ? 'INVALID RANGE' : solutions.join(' ')
  end

  def self.valid?(num)
    num_digits = num.to_s.size
    num_squared = (num**2).to_s
    num == num_squared.slice!(0...-num_digits).to_i + num_squared.to_i
  end
end

puts KaprekarNumber.find_all(gets.to_i, gets.to_i)
