def rotation_point(rotated_list):
  l = 0
  r = len(rotated_list)-1
  while (l < r) :
    if rotated_list[l] <= rotated_list[r]:
      return l
    else:
      mid = (l+r)//2
      if rotated_list[mid] > rotated_list[r]:
        l = mid+1
      else:
        r = mid

  return l