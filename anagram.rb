# Enter your code here. Read input from STDIN. Print output to STDOUT
def anagram_solver(word)
    return "-1" if word.length % 2 == 1
    middle = word.length / 2
    a = word[0..(middle - 1)].split(//)
    b = word[middle..-1].split(//)
    a.each do |char|
        b.delete_at(b.index(char)) if b.include?(char)
    end
    return b.length
end
t = gets.to_i
t.times do 
    puts anagram_solver(gets.chomp)
end