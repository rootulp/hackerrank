class SherlockAndArray
  attr_reader :arr
  def initialize(elements)
    @arr = elements.split(' ').map(&:to_i)
  end

  def solve
    valid_mid? ? 'YES' : 'NO'
  end

  def valid_mid?
    return true if arr.size == 1

    left = 0
    right = arr.reduce(:+)
    arr.each_index do |i|
      right -= arr[i]
      next if i.zero?
      left += arr[i - 1]
      return true if left == right
    end

    false
  end
end

num_cases = gets.to_i
num_cases.times do
  _ = gets.to_i
  puts SherlockAndArray.new(gets).solve
end
