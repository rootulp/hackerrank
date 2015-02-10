class AlmostSorted
  attr_reader :sorted
  attr_accessor :arr, :left, :right
  def initialize(elements)
    @arr = elements.split(" ").map{|x| x.to_i}
    @sorted = arr.sort
    @left = find_left
    @right = find_right
  end

  def solve
    return "yes" if sorted?
    return "yes\nswap #{left+1} #{right+1}" if swappable?(left, right)
    return "yes\nreverse #{left+1} #{right+1}" if reversable?(left, right)
    return "no"
  end

  private

  def sorted?
    sorted == arr
  end

  def swappable?(index1, index2)
    swap(index1, index2) #swap vals
    swappable = sorted?
    swap(index1, index2) #undo swap
    swappable
  end

  def reversable?(index1, index2)
    swap_reverse(index1, index2) #reverse subarr
    reversable = sorted?
    swap_reverse(index1, index2) #undo reverse
    reversable
  end

  def find_left
    arr.each_with_index do |val, i|
      return i if i != arr.length-1 && val > arr[i+1]
    end
  end
      
  def find_right
    arr.reverse.each_with_index do |val, i|
      return arr.length-i-1 if i != arr.length-1 && val < arr.reverse[i+1]
    end
  end

  def swap(a, b)
    arr[a], arr[b] = arr[b], arr[a]
  end

  def swap_reverse(a, b)
    arr[a..b] = arr[a..b].reverse
  end
end

n = gets.to_i
test = AlmostSorted.new(gets)
puts test.solve