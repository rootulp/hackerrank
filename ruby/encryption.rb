rectangle = []
result = ''
phrase = gets.gsub(/\s+/, '').split(//)
cols = (phrase.length**0.5).ceil
phrase.each_slice(cols) { |row| rectangle << row }
encoded = rectangle.first.zip(*rectangle.drop(1))
encoded.each { |col| result << col.join + ' ' }
puts result
