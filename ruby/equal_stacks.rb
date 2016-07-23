# Equal Stacks
class EqualStacks
  attr_accessor :stacks
  def initialize(stacks)
    @stacks = stacks
  end

  def equalize_stacks
    pop_largest_stack until equal_stacks?
    largest_stack.height
  end

  def pop_largest_stack
    largest_stack.pop
  end

  def equal_stacks?
    largest_stack.height == smallest_stack.height
  end

  def largest_stack
    stacks.max_by(&:height)
  end

  def smallest_stack
    stacks.min_by(&:height)
  end
end

# Stack
class Stack
  attr_accessor :heights, :height
  def initialize(heights)
    @heights = heights
    @height = heights.reduce(:+)
  end

  def pop
    @height -= heights.shift
  end
end

_ = gets.chomp
stacks = Array.new(3) { Stack.new(gets.chomp.split(' ').map(&:to_i)) }
puts EqualStacks.new(stacks).equalize_stacks
