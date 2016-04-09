# Bigger is Greater
class BiggerIsGreater
  def self.next_lexicographically(str)
    return 'no answer' unless find_k(str)
    k = find_k(str)
    i = find_i(str, k)
    reverse_after(swap(str, k, i), k)
  end

  def self.find_k(str)
    (str.size - 2).downto(0) do |x|
      return x if str[x] < str[x + 1]
    end
    false
  end

  def self.find_i(str, k)
    (str.size - 1).downto(k + 1) do |x|
      return x if str[k] < str[x]
    end
  end

  def self.swap(str, k, i)
    str[k], str[i] = str[i], str[k]
    str
  end

  def self.reverse_after(str, k)
    str[0..k] + str[k + 1..-1].reverse
  end

  private_class_method :find_k, :find_i, :swap, :reverse_after
end

t = gets.to_i
t.times do
  puts BiggerIsGreater.next_lexicographically(gets.chomp)
end

# The algorithm implemented here is used to generate the next string in
# lexographic order. The algorithm can be found here:
# https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
# Pseudocode is below (also the reason for cryptic variable names)
# Find the largest index k such that a[k] < a[k + 1]. If no such index exists,
# the permutation is the last permutation.
# Find the largest index l greater than k such that a[k] < a[l].
# Swap the value of a[k] with that of a[l].
# Reverse the sequence from a[k + 1] up to and including the final element a[n].
