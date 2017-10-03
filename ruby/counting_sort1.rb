class CountingSort
  attr_reader :arr, :counts
  def initialize(elements)
    @arr = elements.split(' ').map(&:to_i)
    @counts = build_counts
  end

  def build_counts
    counts = Hash.new(0)
    arr.each { |val| counts[val] += 1 }
    counts
  end

  def print_counts
    (0..99).each do |val|
      print "#{counts[val]} "
    end
  end
end

_ = gets.to_i
test_case = CountingSort.new(gets.chomp)
test_case.print_counts
