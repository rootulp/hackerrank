# Time Conversion
class TimeConversion
  def self.convert(time)
    # Reset noon to midnight
    hours = time.slice!(0, 2)
    hours = '00' if hours == '12'

    # Add 12 hours if PM
    period = time.slice!(-2, 2)
    period == 'AM' ? "#{hours}#{time}" : "#{hours.to_i + 12}#{time}"
  end
end

time = gets.chomp
puts TimeConversion.convert(time)
