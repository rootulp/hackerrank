# Angry Professor
class AngryProfessor
  def self.cancel?(student_times, cancel_threshold)
    present_at_start(student_times) < cancel_threshold ? 'YES' : 'NO'
  end

  def self.present_at_start(student_times)
    student_times.count { |time| time <= 0 }
  end
end

t = gets.to_i
t.times do
  _, cancel_threshold = gets.split(' ').map(&:to_i)
  student_times = gets.split(' ').map(&:to_i)
  puts AngryProfessor.cancel?(student_times, cancel_threshold)
end
