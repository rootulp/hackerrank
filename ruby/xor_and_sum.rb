# Xor and Sum
class XorAndSum
  UPPER_BOUND = 314_159
  MODULO_VAL = (10**9) + 7

  def self.calculate(a, b)
    sum = 0
    (0..UPPER_BOUND).each { |i| sum += (a ^ (b << i)) }
    sum % MODULO_VAL
  end
end

a = gets.to_i(2)
b = gets.to_i(2)
puts XorAndSum.calculate(a, b)
