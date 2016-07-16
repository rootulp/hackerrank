# Pairs
class Pairs
  attr_reader :k, :integers, :left, :right, :pairs
  def initialize(k, integers)
    @k = k
    @integers = integers.sort
    @left = 0
    @right = 0
    @pairs = 0
    calculate_pairs
  end

  private

  def calculate_pairs
    until reached_end?(left)
      increment_pairs if difference_equals_k?(integers[left], integers[right])
      move_pointers
    end
  end

  def move_pointers
    if integers[right] - integers[left] < k && !reached_end?(right)
      increment_right
    else
      increment_left
    end
  end

  def difference_equals_k?(int1, int2)
    int2 - int1 == k
  end

  def reached_end?(index)
    index == integers.size - 1
  end

  def increment_left
    @left += 1
  end

  def increment_right
    @right += 1
  end

  def increment_pairs
    @pairs += 1
  end
end

_, k = gets.split(' ').map(&:to_i)
integers = gets.split(' ').map(&:to_i)
puts Pairs.new(k, integers).pairs
