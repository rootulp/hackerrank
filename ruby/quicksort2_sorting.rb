def quickSort(ar)
  return ar if ar.length <= 1

  pivot = ar.shift
  pivot_ar = [pivot] # Used later to concat arrays
  left = []
  right = []

  ar.each do |val|
    left << val if val < pivot
    right << val if val > pivot
  end

  partial = quickSort(left) + pivot_ar + quickSort(right)
  puts partial.join(' ')
  partial
end

_ = gets.to_i
ar = gets.chomp.split.map(&:to_i)
quickSort(ar)
