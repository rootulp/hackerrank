_, k, q = gets.split(' ').map(&:to_i)
arr = gets.split(' ').map(&:to_i)
k.times { arr.unshift(arr.pop) }
q.times { puts arr[gets.to_i] }
