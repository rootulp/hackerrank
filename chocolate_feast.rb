def compute_chocolate(dollars, cost, wrappers_for_free)
    chocolate = dollars / cost
    return chocolate + exchange(chocolate, wrappers_for_free)
end

def exchange(wrappers, wrappers_for_free)
  return 0 if wrappers < wrappers_for_free
    divmod = wrappers.divmod(wrappers_for_free)
    free_chocolate = divmod[0]
    extra = divmod[1]

  if extra == 0 && free_chocolate < wrappers_for_free
    return free_chocolate
  else
    return free_chocolate + exchange(free_chocolate + extra, wrappers_for_free)
  end
end

t = gets.to_i
t.times{
    (dollars, cost, wrappers_for_free) = gets.split.map{|i| i.to_i}
    puts compute_chocolate(dollars, cost, wrappers_for_free)
}
