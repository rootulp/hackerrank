# Funny String
class FunnyString
  attr_reader :str, :rev
  def initialize(str)
    @str = str
    @rev = str.reverse
  end

  def answer
    funny? ? 'Funny' : 'Not Funny'
  end

  def funny?
    compute_ords(str) == compute_ords(rev)
  end

  def compute_ords(set)
    set.chars.each_cons(2).with_object([]) do |arr, memo|
      memo << (arr.first.ord - arr.last.ord).abs
    end
  end
end

gets.to_i.times { puts FunnyString.new(gets.chomp).answer }
