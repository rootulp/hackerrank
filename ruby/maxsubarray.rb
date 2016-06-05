# Max Subarray
class MaxSubArray
  def self.contiguous(arr)
    return arr.max if all_negative?(arr)
    total = 0
    arr.map { |x| total = total + x > 0 ? total + x : 0 }.max
  end

  def self.non_contiguous(arr)
    return arr.max if all_negative?(arr)
    arr.select { |x| x > 0 }.reduce(:+)
  end

  def self.all_negative?(arr)
    arr.select { |x| x > 0 }.empty?
  end
end

t = gets.to_i
t.times do
  _ = gets.to_i
  arr = gets.split(' ').map(&:to_i)
  puts "#{MaxSubArray.contiguous(arr)} #{MaxSubArray.non_contiguous(arr)}"
end
