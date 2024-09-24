def move_duplicates(dupe_list):
  unique_idx = 0
  for i in range(len(dupe_list) - 1):
    if dupe_list[i] != dupe_list[i + 1]:
      dupe_list[i], dupe_list[unique_idx] = dupe_list[unique_idx], dupe_list[i]
      unique_idx += 1
  dupe_list[unique_idx], dupe_list[len(dupe_list) - 1] = dupe_list[len(dupe_list) - 1], dupe_list[unique_idx]
  return unique_idx


x = [1, 1, 2, 2,2, 3, 4, 5, 5, 6, 7, 7]

print(move_duplicates(x)) # 6
print(x)