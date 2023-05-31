# solution for senior 2023 question 3

from copy import deepcopy as cp
from os import system

class Grid:
  nums = [] # nums[row][colum]
  colums_asymmetry = [] # 1 for not symmetric
  rows_asymmetry = []
  def __init__(self, n, m): # n and m is the number of rows and colums
    self.nums = [[0 for i in range(m)] for j in range(n)]
    self.colums_asymmetry = [0 for i in range(m)]
    self.rows_asymmetry = [0 for i in range(n)]
    
  def update(self, row, col, value):
    self.nums[row][col] = value
    row_asymmetry = 0
    for i in range(int(len(self.colums_asymmetry)/2)):
      if self.nums[row][i] != self.nums[row][-1-i]:
        row_asymmetry = 1
        break
    self.rows_asymmetry[row] = row_asymmetry
    
    col_asymmetry = 0
    for i in range(int(len(self.rows_asymmetry)/2)):
      if self.nums[i][col] != self.nums[-1-i][col]:
        col_asymmetry = 1
        break
    self.colums_asymmetry[col] = col_asymmetry
    
  def equals(self, grid):
    for i in range(len(self.rows_asymmetry)):
      for j in range(len(self.cols_asymmetry)):
        if grid.nums[i][j] != self.nums[i][j]:
          return False
    return True
    
  def get_number_of_asymmetric_rows(self):
    result = 0
    for i in self.rows_asymmetry:
      result += i
    return result
  
  def get_number_of_asymmetric_colums(self):
    result = 0
    for i in self.colums_asymmetry:
      result += i
    return result
    
  def copy(self):
    copied_self = Grid(n, m)
    copied_self.nums = cp(self.nums)
    copied_self.rows_asymmetry = cp(self.rows_asymmetry)
    copied_self.colums_asymmetry = cp(self.colums_asymmetry)
    return copied_self
    
  def __str__(self):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    string = ""
    for i in range(len(self.rows_asymmetry)):
      for j in range(len(self.colums_asymmetry)):
        string += alphabet[self.nums[i][j]]
      string += "\n"
    return string

n, m, r, c = input().split()
n = int(n)
m = int(m)
r = n - int(r)
c = m - int(c)
grid = Grid(n, m)

ans = "IMPOSSIBLE"
found = False

path = set()
def dfs(grid:Grid):
  global found, ans
  if grid.get_number_of_asymmetric_rows() == r and grid.get_number_of_asymmetric_colums() == c:
    ans = grid
    found = True
    return
  
  if found:
    return
  
  # go through all the options we can do
  options_both_closing = [] # the options that can make the grid have both r and c closer to the targeted
  options_rows_closing = [] # the options that can make the amount of asymmetric rows approaching the objective quantity
  options_colums_closing = [] # the options for colums
  # TODO better sort all the options of best to worse in the order of how good it is leading to the required r and c
  for i in range(n):
    for j in range(m):
      option = grid.copy()
      if option.nums[i][j] + 1 >= 2:
        continue
      option.update(i, j, option.nums[i][j] + 1)
      if (option.get_number_of_asymmetric_rows(), option.get_number_of_asymmetric_colums()) in path:
        continue
      path.add((option.get_number_of_asymmetric_rows(), option.get_number_of_asymmetric_colums()))
      rows_closing = (option.get_number_of_asymmetric_rows() - grid.get_number_of_asymmetric_rows()) * (r - grid.get_number_of_asymmetric_rows()) > 0 # if we are moving in the right direction in the matter of the amount of asymmetric rpws required
      colums_closing = (option.get_number_of_asymmetric_colums() - grid.get_number_of_asymmetric_colums()) * (c - grid.get_number_of_asymmetric_colums()) > 0 # in the matter of colums
      # print((option.get_number_of_asymmetric_rows(), option.get_number_of_asymmetric_colums(), rows_closing, colums_closing))
      if rows_closing:
        if colums_closing:
          options_both_closing.append(option)
        else:
          options_rows_closing.append(option)
      elif colums_closing:
        options_colums_closing.append(option)
  
  for option in options_both_closing:
    dfs(option)
  for option in options_colums_closing:
    dfs(option)
  for option in options_rows_closing:
    dfs(option)
    
dfs(grid)
print(ans)