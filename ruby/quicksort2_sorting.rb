def  quickSort(ar) 

    if ar.length <= 1
        return ar
    end
    
    pivot = ar.shift
    pivot_ar = [pivot] # Used later to concat arrays
    left = []
    right = []

    ar.each do |val|
        left << val if val < pivot
        right << val if val > pivot
    end

    partial = quickSort(left) + pivot_ar + quickSort(right)
    puts partial.join(" ")
    return partial

end

count = gets.to_i;
ar = gets.chomp.split.map{|x| x.to_i};
quickSort(ar);