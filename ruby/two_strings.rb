# Two Strings
class TwoStrings
  def self.valid_substring(str1, str2)
    substring_helper(str1, str2) ? 'YES' : 'NO'
  end

  def self.substring_helper(str1, str2)
    str2.chars.each { |char| return true if str1.include?(char) }
    false
  end
end

t = gets.to_i
t.times do
  str1 = gets.chomp
  str2 = gets.chomp
  puts TwoStrings.valid_substring(str1, str2)
end
