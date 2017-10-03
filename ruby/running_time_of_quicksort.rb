class InsertionSort
  attr_accessor :arr, :shifts
  def initialize(arr)
    @arr = arr
    @shifts = 0
  end

  def sort
    arr.each_index do |index|
      next if index.zero?
      val = arr.delete_at(index)
      while index > 0 && val < arr[index - 1]
        index -= 1
        @shifts += 1
      end
      arr.insert(index, val)
    end
  end
end

class QuickSort
  attr_accessor :arr, :swaps
  def initialize(arr)
    @arr = arr
    @swaps = 0
  end

  def sort(first_i = 0, pivot_i = arr.size - 1)
    last_i = pivot_i - 1
    insert_i = first_i
    return if first_i > last_i

    (first_i..last_i).each do |i|
      if arr[i] < arr[pivot_i]
        swap(i, insert_i)
        insert_i += 1
      end
    end

    swap(pivot_i, insert_i)
    sort(first_i, insert_i - 1)
    sort(insert_i + 1, pivot_i)
  end

  def swap(a, b)
    arr[a], arr[b] = arr[b], arr[a]
    @swaps += 1
  end
end

_ = gets.to_i
arr1 = gets.chomp.split(' ').map(&:to_i)
arr2 = arr1.dup

quick = QuickSort.new(arr1)
insertion = InsertionSort.new(arr2)

quick.sort
insertion.sort

puts (insertion.shifts - quick.swaps).to_s
