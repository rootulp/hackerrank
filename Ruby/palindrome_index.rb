class PalindromeIndex
  attr_reader :str, :arr
  def initialize(str)
    @str = str
    @arr = str.split(//)
  end

  def index_to_remove
    return -1 if palindrome?(str)
    arr.each_index do |i|
      j = arr.size - 1 - i
      if arr[i] != arr[j]
        return i_or_j(i, j)
        # return i if palindrome?(remove_at(i))
        # return j if palindrome?(remove_at(i))
      end
    end
  end

  def i_or_j(i, j)
    if str[i+1] == str[j] && str[i] == str[j-1]
      if str[i+1] == str[j-2]
        return j
      elsif str[i+2] == str[j-1]
        return i
      end
    else 
      if str[i+1] == str[j]
        return i
      elsif str[i] == str[j-1]
        return j
      end
    end
  end

  def remove_at(index)
    if index == 0
      str[1..-1]
    elsif index == str.length
      str[0..str.length-1]
    else
      str[0..index-1] + str[index+1..-1]
    end
  end

  def palindrome?(str)
    str == str.reverse
  end

end

num_cases = gets.to_i
num_cases.times do
  test_case = PalindromeIndex.new(gets.chomp)
  puts test_case.index_to_remove
end