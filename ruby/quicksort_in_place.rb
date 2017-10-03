class QuickSort
  attr_accessor :arr
  def initialize(elements)
    @arr = elements.split(' ').map(&:to_i)
  end

  def sort(first_i = 0, last_i = arr.size - 2)
    # Stop if already sorted
    return if first_i > last_i

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
    print_arr

    # Recursively sort left and ride sides
    sort(first_i, insert_i - 2)
    sort(insert_i + 1, last_i)
  end

  private

  def swap(a, b)
    arr[a], arr[b] = arr[b], arr[a]
  end

  def print_arr
    puts arr.join(' ')
  end
end

_ = gets.to_i
QuickSort.new(gets).sort
