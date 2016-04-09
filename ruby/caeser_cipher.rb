# Caesar Cipher
class CaesarCipher
  def self.encrypt(word, k)
    word.chars.map { |char| encrypt_char(char, k) }.join
  end

  def self.encrypt_char(char, k)
    return encrypt_lower(char, k) if /[a-z]/ =~ char
    return encrypt_upper(char, k) if /[A-Z]/ =~ char
    char
  end

  def self.encrypt_upper(char, k)
    (((char.ord - 65 + k) % 26) + 65).chr
  end

  def self.encrypt_lower(char, k)
    (((char.ord - 97 + k) % 26) + 97).chr
  end

  private_class_method :encrypt_char, :encrypt_upper, :encrypt_lower
end

_ = gets
word = gets.chomp
k = gets.to_i
puts CaesarCipher.encrypt(word, k)
