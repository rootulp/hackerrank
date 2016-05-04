# Flowers
class Flowers
  attr_reader :k, :total
  def initialize(k, flowers)
    @k = k
    @total = next_c(flowers.sort, 1)
  end

  def next_c(flowers, c)
    flowers.any? ? (c * flowers.pop(k).reduce(:+)) + next_c(flowers, c + 1) : 0
  end
end

_, k = gets.split(' ').map(&:to_i)
flowers = gets.split(' ').map(&:to_i)
puts Flowers.new(k, flowers).total
