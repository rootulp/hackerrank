def  insertionSort(ar)
    (1..ar.length-1).each do |i|
        val = ar.delete_at(i)

        index = i
        index -= 1 while index > 0 && val < ar[index -1]

        ar.insert(index, val)
        puts ar.join(" ")
  end
end

count = gets.to_i
ar = gets.strip.split.map {|i| i.to_i}
insertionSort(ar)
