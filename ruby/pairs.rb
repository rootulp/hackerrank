# Pairs
class Pairs
  attr_reader :num_pairs
  def initialize(k, arr)
    @num_pairs = calculate_num_pairs(k, arr.sort)
  end

  private

  def calculate_num_pairs(k, arr)
    pairs = 0
    left = 0
    right = 0

    loop do
      return pairs if left == arr.size - 1

      if left == right || arr[right] - arr[left] < k
        right == arr.size - 1 ? left += 1 : right += 1
      else
        pairs += 1 if arr[right] - arr[left] == k
        left += 1
      end
    end
  end
end

_, k = gets.split(' ').map(&:to_i)
arr = gets.split(' ').map(&:to_i)
puts Pairs.new(k, arr).num_pairs
