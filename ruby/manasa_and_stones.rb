def last_stone(stones, a, b)
    results = []
    for i in 0..stones do
        results << (i*a) + ((stones-i)*b)
        results << (i*b) + ((stones-i)*a)
    end
    puts results.uniq.sort.join(" ")
end

t = gets.to_i
t.times{
    stones = gets.to_i
    a = gets.to_i
    b = gets.to_i
    last_stone(stones-1, a, b)
}
