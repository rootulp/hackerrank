# Triplet Comparator
class TripletComparator
  def self.scores(a_triplet, b_triplet)
    "#{a_score(a_triplet, b_triplet)} #{b_score(a_triplet, b_triplet)}"
  end

  def self.a_score(a_triplet, b_triplet)
    a_triplet.zip(b_triplet).count { |a, b| a > b }
  end

  def self.b_score(a_triplet, b_triplet)
    a_triplet.zip(b_triplet).count { |a, b| a < b }
  end
end

a_triplet = gets.strip.split(' ').map(&:to_i)
b_triplet = gets.strip.split(' ').map(&:to_i)
puts TripletComparator.scores(a_triplet, b_triplet)
