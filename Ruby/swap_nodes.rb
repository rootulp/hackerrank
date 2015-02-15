class BinaryTree
  def initialize(num_nodes)
    @data = Array.new(num_nodes)
  end

  def add(val)
    @data << val
  end

  def swap(index)

  end

  def inorder

  end
end

num_nodes = gets.to_i
test_case = BinaryTree.new(num_nodes)
