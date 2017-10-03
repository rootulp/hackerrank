class SherlockAndPairs
  attr_reader :arr, :counts
  def initialize(elements)
    @arr = elements.split(' ').map(&:to_i)
    @counts = find_counts
  end

  def pairs
    total = 0
    counts.each do |_key, value|
      next if value == 1
      total += value * (value - 1)
    end
    total
  end

  def find_counts
    counts = Hash.new 0
    arr.each { |x| counts[x] += 1 }
    counts
  end
end

num_cases = gets.to_i
num_cases.times do
  _ = gets.to_i
  test_case = SherlockAndPairs.new(gets)
  puts test_case.pairs
end
