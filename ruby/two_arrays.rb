# Two Arrays
class TwoArrays
  attr_reader :valid
  def initialize(arr1, arr2, k)
    @valid = valid?(arr1.sort, arr2.sort.reverse, k) ? 'YES' : 'NO'
  end

  def valid?(arr1, arr2, k)
    arr1.map.with_index { |x, i| x + arr2[i] }.select { |x| x < k }.empty?
  end
end

t = gets.to_i
t.times do
  _, k = gets.split(' ').map(&:to_i)
  arr1 = gets.split(' ').map(&:to_i)
  arr2 = gets.split(' ').map(&:to_i)
  puts TwoArrays.new(arr1, arr2, k).valid
end
