# Mark and Toys
class MarkAndToys
  attr_reader :total_toys
  def initialize(money, prices)
    @total_toys = one_more_toy(money, prices.sort)
  end

  private

  def one_more_toy(money, prices)
    money -= prices.shift
    money <= 0 ? 0 : 1 + one_more_toy(money, prices)
  end
end

_, money = gets.split(' ').map(&:to_i)
prices = gets.split(' ').map(&:to_i)
puts MarkAndToys.new(money, prices).total_toys
