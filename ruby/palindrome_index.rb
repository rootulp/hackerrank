# Palindrome Index
class PalindromeIndex
  attr_reader :str, :chars
  def initialize(str)
    @str = str
    @chars = str.chars
  end

  def index_to_remove
    chars.each_index do |i|
      j = chars.size - 1 - i
      return i_or_j(i, j) if chars[i] != chars[j]
    end
    -1
  end

  private

  def i_or_j(i, j)
    if i_next_to_j(i, j) && str[i + 2] == str[j - 1]
      i
    elsif i_next_to_j(i, j) && str[i + 1] == str[j - 2]
      j
    else
      i_or_j_helper(i, j)
    end
  end

  def i_next_to_j(i, j)
    str[i + 1] == str[j] && str[i] == str[j - 1]
  end

  def i_or_j_helper(i, j)
    if str[i + 1] == str[j]
      i
    elsif str[i] == str[j - 1]
      j
    end
  end
end

num_cases = gets.to_i
num_cases.times do
  test_case = PalindromeIndex.new(gets.chomp)
  puts test_case.index_to_remove
end
