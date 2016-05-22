# Sherlock Anagrams
class SherlockAnagrams
  attr_reader :str
  def initialize(str)
    @str = str
  end

  def num_unordered_pairs
    sorted_substring_occurences.values.reduce(0) do |memo, val|
      memo += n_choose_r(val, 2)
    end
  end

  private

  def sorted_substring_occurences
    sorted_substrings.each_with_object(Hash.new(0)) do |substring, occurences|
      occurences[substring] += 1
    end
  end

  def sorted_substrings
    (1..str.size - 1).each_with_object([]) do |i, substrings|
      str.chars.each_cons(i) do |substring|
        substrings << substring.sort.join
      end
    end
  end

  def factorial(n)
    (1..n).inject(:*) || 1
  end

  def n_choose_r(n, r)
    factorial(n) / (factorial(r) * factorial(n - r))
  end
end

t = gets.to_i
t.times do
  puts SherlockAnagrams.new(gets.chomp).num_unordered_pairs
end
