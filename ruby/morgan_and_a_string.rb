class MorganString
  attr_reader :min_string
  def initialize(str1, str2)
    @str1 = str1
    @str2 = str2
    @min_string = next_letter(str1.split(//), str2.split(//))
  end

  def next_letter(stack1, stack2)
    return '' if stack1.empty? && stack2.empty?

    if stack1.empty?
      stack2.join
    elsif stack2.empty?
      stack1.join
    elsif stack1.first <= stack2.first
      stack1.shift + next_letter(stack1, stack2)
    else
      stack2.shift + next_letter(stack1, stack2)
    end
  end
end

t = gets.to_i
t.times do
  str1 = gets.chomp
  str2 = gets.chomp
  puts MorganString.new(str1, str2).min_string
end
