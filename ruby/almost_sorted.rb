class AlmostSorted

  attr_reader :arr
  def initialize(elements)
    @arr = elements.split(" ").map { |x| x.to_i }
  end

  def solve
    left = find_left
    right = find_right
    if left && right
      if ascending?(swap(arr.clone, left, right))
        return "yes\nswap #{left+1} #{right+1}"
      elsif ascending?(reverse(arr.clone, left, right))
        return "yes\nreverse #{left+1} #{right+1}"
      else
        return 'no'
      end
    end
  end

  private

  def find_left
    (0).upto(arr.size-2) do |x|
      return x if arr[x] > arr[x+1]
    end
    false
  end

  def find_right
    (arr.size-1).downto(1) do |x|
      return x if arr[x] < arr[x-1]
    end
    false
  end

  def ascending?(arr)
    arr.each_cons(2).all?{ |i, j| i <= j }
  end

  def swap(arr, left, right)
    arr[left], arr[right] = arr[right], arr[left]
    arr
  end

  def reverse(arr, left, right)
    arr[0..left-1] + arr[left..right].reverse + arr[right+1..-1]
  end

end

gets.to_i
puts AlmostSorted.new(gets).solve
