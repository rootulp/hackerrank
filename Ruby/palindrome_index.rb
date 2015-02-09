class PalindromeIndex
  attr_reader :str, :arr
  def initialize(str)
    @str = str
    @arr = str.split(//)
  end

  def index_to_remove
    arr.each_index do |i|
      j = arr.size - 1 - i
      return i_or_j(i, j) if arr[i] != arr[j]
    end
    return -1
  end

  private

  def i_or_j(i, j)
    if str[i+1] == str[j] && str[i] == str[j-1] && str[i+2] == str[j-1]
      return i
    elsif str[i+1] == str[j] && str[i] == str[j-1] && str[i+1] == str[j-2]
      return j
    elsif str[i+1] == str[j]
      return i
    elsif str[i] == str[j-1]
      return j
    end
  end

end

num_cases = gets.to_i
num_cases.times do
  test_case = PalindromeIndex.new(gets.chomp)
  puts test_case.index_to_remove
end