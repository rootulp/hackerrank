class InsertionSort
  attr_reader :arr
  def initialize(str)
    @arr = str.strip.split.map(&:to_i)
  end

  def sort
    arr.each_index do |index|
      next if index == 0
      val = arr.delete_at(index)
      index -= 1 while index > 0 && val < arr[index - 1]
      arr.insert(index, val)
      puts arr.join(' ')
    end
  end
end

_ = gets.to_i
test_case = InsertionSort.new(gets)
test_case.sort
