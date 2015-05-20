class BiggerIsGreater
  attr_reader :str
  def initialize(str)
    @str = str
  end

  def perms
    str.chars.permutation.map(&:join)
  end

  def acceptable
    perms.select { |perm| perm > str }.sort
  end

  def bigger
    acceptable.empty? ? 'no answer' : acceptable.shift
  end

end

t = gets.to_i
t.times do
  puts BiggerIsGreater.new(gets.chomp).bigger
end
