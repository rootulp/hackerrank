# Make It Anagram
class MakeItAnagram
  attr_reader :str1, :str2
  def initialize(str1, str2)
    @str1 = str1
    @str2 = str2
  end

  def solve
    diff_chars(find_counts(str1), find_counts(str2))
  end

  private

  def find_counts(str)
    counts = Hash.new(0)
    str.each_char { |char| counts[char] += 1 }
    counts
  end

  def diff_chars(counts1, counts2)
    total = 0
    ('a'..'z').each { |char| total += (counts1[char] - counts2[char]).abs }
    total
  end
end

str1 = gets.chomp
str2 = gets.chomp
test_case = MakeItAnagram.new(str1, str2)
puts test_case.solve
