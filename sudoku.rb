class Sudoku
  attr_reader :board

  def initialize(board)
    @board = board.split(//)
  end

  def solve

  end

end

test_cases = gets.to_i

test_cases.times do
    board = ""
    9.times {board << gets.gsub(/\s+/, "")}

    test_game = Sudoku.new(board)
    test_game.solve
    puts test_game.board
end
