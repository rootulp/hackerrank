# Jim and the Orders
class JimAndTheOrders
  def initialize
    @orders = []
  end

  def add_order(customer_num, input_time, process_time)
    @orders << [input_time + process_time, customer_num]
  end

  def output_order
    @orders.sort_by(&:first).map(:last).join(' ')
  end
end

burger_joint = JimAndTheOrders.new

total_customers = gets.to_i
total_customers.times do |customer_num|
  input_time, process_time = gets.split(' ').map(:to_i)
  burger_joint.add_order(customer_num + 1, input_time, process_time)
end

puts burger_joint.output_order
