def compute_chocolate(dollars, cost, wrappers_for_free)
  chocolate = dollars / cost
  chocolate + exchange(chocolate, wrappers_for_free)
end

def exchange(wrappers, wrappers_for_free)
  return 0 if wrappers < wrappers_for_free
  divmod = wrappers.divmod(wrappers_for_free)
  free_chocolate = divmod[0]
  extra = divmod[1]

  if extra == 0 && free_chocolate < wrappers_for_free
    free_chocolate
  else
    free_chocolate + exchange(free_chocolate + extra, wrappers_for_free)
  end
end

t = gets.to_i
t.times do
  (dollars, cost, wrappers_for_free) = gets.split.map(&:to_i)
  puts compute_chocolate(dollars, cost, wrappers_for_free)
end
