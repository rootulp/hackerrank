n = gets.to_i
test_cases = []
results = []
n.times {|x| test_cases.push(gets.chomp)}

def analyze(test_arr, num_reductions)
    if test_arr.length <= 1
        return num_reductions
    else
        x = test_arr.pop
        y = test_arr.shift
        num_reductions += num_reductions_for_pair(x, y, 0)
        return analyze(test_arr, num_reductions)
    end
end

def num_reductions_for_pair(x, y, counter)
    comparison = x <=> y
    if  comparison == 1 
        return num_reductions_for_pair((x.ord - 1).chr, y, counter + 1)
    elsif comparison == -1
        return num_reductions_for_pair(x, (y.ord - 1).chr, counter + 1)
    else
        return counter
    end
end

test_cases.each do |test_str|
    test_arr = test_str.split(//)
    puts analyze(test_arr, 0)
end