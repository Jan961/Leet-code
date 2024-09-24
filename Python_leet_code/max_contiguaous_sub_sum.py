def maximum_sub_sum(my_list):

  max_sum = my_list[0]
  reset = True
  for i in range(len(my_list)):
    if reset:
      curr_best = my_list[i]
      reset = False
    else:
      curr_best = curr_best+ my_list[i]
      if curr_best >  max_sum:
        max_sum = curr_best
      elif curr_best < 0:
        reset = True

  return max_sum