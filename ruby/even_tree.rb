require 'set'

# Node
class Node
  attr_accessor :adjacents
  def initialize
    @adjacents = Set.new
  end
end

# Graph
class Graph
  attr_accessor :nodes, :edges
  def initialize
    @nodes = []
    @edges = []
  end

  def add_node
    nodes << Node.new
  end

  def add_edge(node_a, node_b)
    node_a.adjacents << node_b
    node_b.adjacents << node_a

    edges << [node_a, node_b]
  end

  def self.even_edge?(edge)
    node_a, node_b = edge
    even_subtree?(node_a, node_b) && even_subtree?(node_b, node_a)
  end

  def self.even_subtree?(node_a, node_b)
    subtree(node_a, node_b).size.even?
  end

  # subtree returns an array of the child nodes for 'node' excluding from_node
  # uses a breadth first search
  def self.subtree(node, from_node)
    queue = [node]
    visited = [node]
    while queue.any?
      curr_node = queue.shift
      curr_node.adjacents.each do |adjacent_node|
        next if visited.include?(adjacent_node) || adjacent_node == from_node
        queue << adjacent_node
        visited << adjacent_node
      end
    end
    visited
  end
end

graph = Graph.new
n, m = gets.split(' ').map(&:to_i)
n.times { graph.add_node }
m.times do
  a, b = gets.split(' ').map(&:to_i)
  graph.add_edge(graph.nodes[a - 1], graph.nodes[b - 1])
end
puts graph.edges.count { |edge| Graph.even_edge?(edge) }
