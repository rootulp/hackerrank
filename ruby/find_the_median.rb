class FindTheMedian
  attr_accessor :arr
  def initialize(elements)
    @arr = elements.split(' ').map(&:to_i)
  end

  def find_median(first_i = 0, last_i = arr.size - 2)
    median_i = (arr.size - 1) / 2

    # Stop if already sorted
    return arr[median_i] if first_i > last_i

    # Declare index var's for easier ref
    insert_i = first_i
    pivot_i = last_i + 1

    # Partition
    (first_i..last_i).each do |i|
      next unless arr[i] < arr[pivot_i]
      # Move smaller elements to left
      swap(i, insert_i)
      insert_i += 1
    end
    # Move pivot inbetween left(smaller elements) & right(larger elements)
    swap(pivot_i, insert_i)

    if insert_i == median_i
      return arr[insert_i]
    elsif insert_i > median_i
      find_median(first_i, insert_i - 2)
    elsif insert_i < median_i
      find_median(insert_i + 1, last_i)
    end
  end

  private

  def swap(a, b)
    arr[a], arr[b] = arr[b], arr[a]
  end
end

_ = gets.to_i
puts FindTheMedian.new(gets).find_median
