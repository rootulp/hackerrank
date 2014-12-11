test_string = gets.chomp.downcase
alphabet = ("a".."z").to_a
test_string.split(//).each do |char|
  alphabet.delete(char)
end

if alphabet.empty?
  puts "pangram"
else
  puts "not pangram"
end