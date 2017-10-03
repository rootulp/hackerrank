def insertion_sort(ar)
  shifts = 0
  (1..ar.length - 1).each do |i|
    val = ar.delete_at(i)
    index = i

    while index > 0 && val < ar[index - 1]
      index -= 1
      shifts += 1
    end

    ar.insert(index, val)
  end
  puts shifts
end

_ = gets.to_i
ar = gets.strip.split.map(&:to_i)
insertion_sort(ar)
