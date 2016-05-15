# Song of Pi
class SongOfPi
  PI_VALS = '31415926535897932384626433833'.freeze

  def self.valid?(song)
    song.split(' ').each_with_index do |word, index|
      return "It's not a pi song." if word.length != PI_VALS[index].to_i
    end
    "It's a pi song."
  end
end

t = gets.to_i
t.times do
  puts SongOfPi.valid?(gets)
end
