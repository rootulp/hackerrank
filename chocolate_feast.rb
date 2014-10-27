def compute_chocolate(n,c,m)
    choc = n / c
    dm = choc.divmod(m)
    choc += dm[0]
    choc += (dm[0] + dm[1])/m    
    return choc
end

t = gets.to_i
t.times{
  (n, c, m) = gets.split.map{|i| i.to_i}
    answer = compute_chocolate(n,c,m)
    puts answer
}
