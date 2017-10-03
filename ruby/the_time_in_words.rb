# The Time
class TheTime
  NUMS_TO_WORDS = {
    30 => 'half', # bug
    29 => 'twenty nine',
    28 => 'twenty eight',
    27 => 'twenty seven',
    26 => 'twenty six',
    25 => 'twenty five',
    24 => 'twenty four',
    23 => 'twenty three',
    22 => 'twenty two',
    21 => 'twenty one',
    20 => 'twenty',
    19 => 'nineteen',
    18 => 'eighteen',
    17 => 'seventeen',
    16 => 'sixteen',
    15 => 'quarter', # bug
    14 => 'fourteen',
    13 => 'thirteen',
    12 => 'twelve',
    11 => 'eleven',
    10 => 'ten',
    9  => 'nine',
    8  => 'eight',
    7  => 'seven',
    6  => 'six',
    5  => 'five',
    4  => 'four',
    3  => 'three',
    2  => 'two',
    1  => 'one'
  }.freeze

  class << self
    def in_words(hr, min)
      if min.zero?
        "#{hours(hr, min)} o' clock"
      elsif [15, 30, 45].include?(min)
        "#{mins(min)} #{action(min)} #{hours(hr, min)}"
      else
        "#{mins(min)} #{plural(min)} #{action(min)} #{hours(hr, min)}"
      end
    end

    def action(min)
      min <= 30 ? 'past' : 'to'
    end

    def plural(min)
      min == 1 ? 'minute' : 'minutes'
    end

    def hours(hr, min)
      min <= 30 ? convert(hr) : convert(hr + 1)
    end

    def mins(min)
      min <= 30 ? convert(min) : convert(60 - min)
    end

    def convert(unit)
      NUMS_TO_WORDS[unit]
    end
  end
end

puts TheTime.in_words(gets.to_i, gets.to_i)
