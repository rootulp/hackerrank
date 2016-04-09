# Anagram
class Anagram
  attr_reader :word, :left, :right
  def initialize(word)
    @word = word
    @left = word.chars[0..(word.length / 2 - 1)].sort
    @right = word.chars[(word.length / 2)..-1].sort
  end

  def solve
    return '-1' if word.length.odd?
    return '0' if left == right
    num_changes
  end

  def num_changes
    left.each do |char|
      index = right.index(char)
      right.delete_at(index) unless index.nil?
    end
    right.length
  end
end

t = gets.chomp.to_i
t.times { puts Anagram.new(gets.chomp).solve }
