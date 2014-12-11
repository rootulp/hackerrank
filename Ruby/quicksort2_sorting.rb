def  partition(ar) 
    if ar.length <= 1
        return ar
    end
    p = ar.shift
    a = []
    b = []
    ar.each do |val|
        a << val if val < p
        b << val if val >= p
    end
    return partition(a) << p << partition(b)
end

def quickSort(ar) 
     puts partition(ar).join(" ")
end

cnt = gets.to_i;
ar = gets.chomp.split.map{|x| x.to_i};
quickSort(ar);