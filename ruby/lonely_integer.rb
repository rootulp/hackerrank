def  lonelyinteger(test_case)
    test_case.each do |num|
        if test_case.count(num) == 1
            return num
        end
    end
end
_ = gets.strip.to_i
test_case = gets.strip.split(" ").map! {|i| i.to_i}
print lonelyinteger(test_case)
