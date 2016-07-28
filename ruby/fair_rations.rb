def fair_rations(subjects)
  return 'NO' if subjects.reduce(:+).odd?
  count = 0
  subjects.each.with_index do |subject, i|
    if subject.odd?
      subjects[i] += 1
      subjects[i + 1] += 1
      count += 2
    end
  end
  count
end

_ = gets.chomp
subjects = gets.chomp.split(' ').map(&:to_i)
puts fair_rations(subjects)
