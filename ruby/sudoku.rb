class Sudoku
  attr_reader :board

  def initialize(board)
    @board = board
    create_rows
    create_cols
    create_boxes
  end

  def solve

    return false unless valid?
    return @board if solved?

    next_0 = @board.index("0")

    (1..9).each do |attempt|
      @board[next_0] = attempt
      return solution if Sudoku.new(@board).solve
    end

    return false
  end

  private

  def valid?
    !duplicates?(@rows) && !duplicates?(@cols) && !duplicates?(@boxes)
  end

  def solved?
    @board.count("0") == 0
  end

  def duplicates?(rows_cols_boxes)
    rows_cols_boxes.each do |row_col_box|
      return true if row_col_box.uniq.length != row_col_box.length
    end
    return false
  end

  def create_rows
    @rows = Array.new(9) {Array.new}

    @board.each_with_index do |value, index|
      next if value == "0"
      @rows[index / 9].push(value)
    end
  end

  def create_cols
    @cols = Array.new(9) {Array.new}

    @board.each_with_index do |value, index|
      next if value == "0"
      @cols[index % 9].push(value)
    end
  end

  def create_boxes
    @boxes = Array.new(9) {Array.new}

    @board.each_with_index do |value, index|
      next if value == "0"
      @boxes[(((index / 9) / 3) * 3) + ((index % 9) / 3)].push(value)
    end
  end

end

test_cases = gets.to_i

test_cases.times do
    board = ""
    9.times {board << gets.gsub(/\s+/, "")}

    test_game = Sudoku.new(board.split(//))
    test_game.solve
    puts test_game.board
end
