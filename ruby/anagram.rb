def anagram_solver(word)

    return "-1" if word.length % 2 == 1

    middle = word.length / 2
    left = word[0..(middle - 1)].split(//).sort
    right = word[middle..-1].split(//).sort

    if left == right
      return "0"
    else 
      left.each do |char|
        index = right.index(char)
        right.delete_at(index) unless index.nil?
      end

      return right.length
    end
    
end

t = gets.to_i

t.times do 
    puts anagram_solver(gets.chomp)
end