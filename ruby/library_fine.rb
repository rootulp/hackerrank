require 'date'

class LibraryFine
  def self.calculate_fine(actual, expected)
    calculate(Date.new(*parse_date(actual)), Date.new(*parse_date(expected)))
  end

  def self.parse_date(date)
    date.split(' ').map(&:to_i).reverse
  end

  def self.calculate(actual_date, expected_date)
    return 0     if actual_date <= expected_date
    return 10_000 if actual_date.year != expected_date.year

    if actual_date.month != expected_date.month
      500 * (actual_date.month - expected_date.month)
    else
      15 * (actual_date.day - expected_date.day)
    end
  end

  private_class_method :parse_date, :calculate
end

puts LibraryFine.calculate_fine(gets.chomp, gets.chomp)
