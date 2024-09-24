dna_1 = "ACCGTT"
dna_2 ="CCAGCA"

def longest_common_subsequence(string_1, string_2):


  grid = [[0 for _ in range(len(string_1))] for _ in range(len(string_2))]

  for row in range(1, len(string_2) + 1):
    for col in range(1, len(string_1) + 1):
      if string_1[col - 1] == string_2[row - 1]:
        grid[row][col] = grid[row - 1][col - 1] +1
      else:
        grid[row][col] = max(grid[row][col - 1], grid[row - 1][col])