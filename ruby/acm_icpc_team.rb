(num_people, topics) = gets.split.map(&:to_i)

people = []
team_topics = []

num_people.times do
  people << gets.chomp
end

teams = people.combination(2).to_a

teams.each do |team|
  topics = (team[0].to_i(2) | team[1].to_i(2)).to_s(2)
  team_topics << topics.count('1')
end

ans = team_topics.max

puts ans
puts team_topics.count(ans)
