def lonelyinteger(test_case)
  test_case.each do |num|
    return num if test_case.count(num) == 1
  end
end
_ = gets.strip.to_i
test_case = gets.strip.split(' ').map!(&:to_i)
print lonelyinteger(test_case)
