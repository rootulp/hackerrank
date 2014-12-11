test_string = gets.chomp.downcase
samples = ("a".."z").to_a
test_string.split(//).each do |char|
  samples.delete(char)
end

if samples.empty?
  puts "pangram"
else
  puts "not pangram"
end