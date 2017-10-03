class HackerRankTweets
  def self.num_mentions(str)
    str.downcase.scan('hackerrank').size
  end
end

t = gets.to_i
str = ''
t.times { str << gets }
puts HackerRankTweets.num_mentions(str)
