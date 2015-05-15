def solve(characters)
  count = 0
  characters.each_with_index do |character, index|
    if index != characters.length
      count += 1 if character == characters[index+1]
    end
  end

  return count
end

t = gets.to_i
t.times {
  characters = gets.chomp.split(//)
  puts solve(characters)
}
