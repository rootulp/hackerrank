def  insertionSort(ar)
    ar.reverse!
    v = ar[0]
    
    if v >= ar[1]
        puts ar.reverse.join(" ")
        return
    end
        
    ar.each_with_index do |x ,index|
        if index == ar.length-1
            ar[index] = v
            puts ar.reverse.join(" ")
            return
        elsif v > ar[index+1]
            ar[index] = v
            puts ar.reverse.join(" ")
            return
        else
            ar[index] = ar[index+1]
            puts ar.reverse.join(" ")
        end
    end     
end

count = gets.to_i
ar = gets.strip.split.map {|i| i.to_i}

insertionSort(ar)
