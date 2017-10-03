def insertionSort(ar)
  ar.reverse!
  v = ar[0]

  # Check if already sorted
  return ar.reverse.join(' ') if v >= ar[1]

  # Itterate over reversed ar, reverse again before returning and printing
  ar.each_with_index do |_x, index|
    # Check if you found the correct spot or reached end of ar
    if v > ar[index + 1] || index == ar.length - 1
      ar[index] = v
      return ar.reverse.join(' ')
    else
      # Replace current element with next element
      ar[index] = ar[index + 1]
      puts ar.reverse.join(' ')
    end
  end
end

_ = gets.to_i
ar = gets.strip.split.map(&:to_i)

puts insertionSort(ar)
