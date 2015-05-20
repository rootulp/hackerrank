class BiggerIsGreater

  attr_reader :str
  def initialize(str)
    @str = str
  end

  def solve
    return 'no answer' unless find_k
    k = find_k
    i = find_i(k)
    swap(k, i)
    reverse_after(k)
    str
  end

  private

  def find_k
    (str.size-2).downto(0) do |x|
      return x if str[x] < str[x+1]
    end
    false
  end

  def find_i(k)
    (str.size-1).downto(k+1) do |x|
      return x if str[k] < str[x]
    end
  end

  def swap(k, i)
    @str[k], @str[i] = @str[i], @str[k]
  end

  def reverse_after(k)
    @str = @str[0..k] + @str[k+1..-1].reverse
  end

end

t = gets.to_i
t.times do
  puts BiggerIsGreater.new(gets.chomp).solve
end

# The algorithm implemented here is used to generate the next string in lexographic order.
# The algorithm can be found here: https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
# Pseudocode is below (also the reason for cryptic variable names)
# Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
# Find the largest index l greater than k such that a[k] < a[l].
# Swap the value of a[k] with that of a[l].
# Reverse the sequence from a[k + 1] up to and including the final element a[n].
