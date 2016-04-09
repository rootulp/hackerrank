# Almost Sorted
class AlmostSorted
  attr_reader :arr
  def initialize(elements)
    @arr = elements.split(' ').map(&:to_i)
  end

  def solve
    l = find_left
    r = find_right
    return 'no' unless l && r
    return "yes\nswap #{l + 1} #{r + 1}" if sorted?(swap(arr.clone, l, r))
    return "yes\nreverse #{l + 1} #{r + 1}" if sorted?(reverse(arr.clone, l, r))
    'no'
  end

  private

  def find_left
    0.upto(arr.size - 2) do |x|
      return x if arr[x] > arr[x + 1]
    end
    false
  end

  def find_right
    (arr.size - 1).downto(1) do |x|
      return x if arr[x] < arr[x - 1]
    end
    false
  end

  def sorted?(arr)
    arr.each_cons(2).all? { |i, j| i <= j }
  end

  def swap(arr, left, right)
    arr[left], arr[right] = arr[right], arr[left]
    arr
  end

  def reverse(arr, left, right)
    arr[0..left - 1] + arr[left..right].reverse + arr[right + 1..-1]
  end
end

gets.to_i
puts AlmostSorted.new(gets).solve
