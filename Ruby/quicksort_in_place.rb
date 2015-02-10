class QuickSort
  attr_accessor :arr
  def initialize(elements)
    @arr = elements.split(" ").map{|x| x.to_i};
  end

  def sort(first_i=0, last_i=arr.size-2)
    return if first_i > last_i

    insert_i = first_i
    pivot_i = last_i + 1
    
    (first_i..last_i).each do |i|
      if arr[i] < arr[pivot_i]
        swap(i, insert_i)
        insert_i += 1
      end
    end
    swap(pivot_i, insert_i)
    print_arr

    #puts "#{first_i}, #{insert_i-2}"
    sort(first_i, insert_i-2)
    #puts "#{insert_i+1}, #{pivot_i-1}"
    sort(insert_i+1, last_i)
  end

  private

  def swap(a, b)
    arr[a], arr[b] = arr[b], arr[a]
  end

  def print_arr
    puts arr.join(" ")
  end
end

n = gets.to_i;
QuickSort.new(gets).sort