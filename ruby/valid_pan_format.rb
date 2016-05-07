# Pan
class PAN
  PAN_REGEX = /[A-Z]{5}\d{4}[A-Z]{1}/
  def self.valid?(str)
    str.match(PAN_REGEX) ? 'YES' : 'NO'
  end
end

t = gets.to_i
t.times do
  puts PAN.valid?(gets)
end
