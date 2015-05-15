class TheTime

  NUMS_TO_WORDS = {
    30 => "half", #bug
    29 => "twenty nine",
    28 => "twenty eight",
    27 => "twenty seven",
    26 => "twenty six",
    25 => "twenty five",
    24 => "twenty four",
    23 => "twenty three",
    22 => "twenty two",
    21 => "twenty one",
    20 => "twenty",
    19 => "nineteen",
    18 => "eighteen",
    17 => "seventeen",
    16 => "sixteen",
    15 => "quarter", #bug
    14 => "fourteen",
    13 => "thirteen",
    12 => "twelve",
    11 => "eleven",
    10 => "ten",
    9  => "nine",
    8  => "eight",
    7  => "seven",
    6  => "six",
    5  => "five",
    4  => "four",
    3  => "three",
    2  => "two",
    1  => "one"
  }

  def self.in_words(hour, min)
    case min
    when 0
      "#{convert(hour)} o' clock"
    when 1..30
      "#{convert(min)} #{minutes_for(min)}past #{convert(hour)}"
    when 31..59
      "#{convert(60 - min)} #{minutes_for(min)}to #{convert(hour + 1)}"
    end

  end

  def self.minutes_for(min)
    case min
    when 15, 30, 45
      ""
    when 1
      "minute "
    else
      "minutes "
    end
  end

  def self.convert(unit)
    "#{NUMS_TO_WORDS[unit]}"
  end

end

puts TheTime.in_words(gets.to_i, gets.to_i)
