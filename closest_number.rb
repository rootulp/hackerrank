t = gets.to_i
t.times do 
    (a,b,x) = gets.split(" ").map{|x| x.to_i}
    num_to_find = a**b
    high = x
    low = high
        
    while high < a**b
        low = high
        high += x
    end
    
    diff_low = (num_to_find - low).abs
    diff_high = (high - num_to_find).abs
    diff_zero = (num_to_find).abs
    
    if diff_zero < diff_low && diff_zero < diff_high
        puts "0"
    elsif diff_low < diff_zero && diff_low < diff_high
        puts low
    else
        puts high
    end
      
end