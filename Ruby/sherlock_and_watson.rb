n, k, q = gets.split(" ").map{|x| x.to_i}
arr = gets.split(" ").map{|x| x.to_i}
k.times {arr.unshift(arr.pop)}
q.times {puts arr[gets.to_i]}
