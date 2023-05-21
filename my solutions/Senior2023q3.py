# solution for senior 2023 question 3

class Grid:
  nums = [] # nums[row][colum]
  colums_asymmetry= [] # 1 for not symmetric
  rows_asymmetry = []
  def __init__(n, m): # n and m is the number of rows and colums
    self.nums = [[0 for i in range(m)] for j in range(n)]
    self.colums_asymmetry = [0 for i in range(m)]
    self.rows_asymmetry = [0 for i in range(n)]
    
  def update(row,col, value):
    nums[row][col] = value
    row_asymmetry = 0
    for i in range(int(len(this.colums_asymmetry)/2)):
      if nums[row][i] != nums[row][-1-i]:
        row_asymmetry = 1
    self.rows_asymmetry[row] = row_asymmetry
    
    col_asymmetry = 0
    for i in range(int(len(this.rows_asymmetry)/2)):
      if nums[i][col] != nums[-1-i][col]:
        col_asymmetry = 1
    self.cols_asymmetry[col] = col_asymmetry
    
  def equals(grid:Grid):
    for i in range(len(self.rows_asymmetry)):
      for j in range(len(self.cols_asymmetry)):
        if grid.nums[i][j] != self.nums[i][j]:
          return False
    return True
    
  def get_number_of_asymmetric_rows():
    result = 0
    for i in self.rows_asymmetry:
      result += i
    return result

n, m, r, c = input().split()
n = int(n)
m = int(m)
r = int(r)
c = int(c)

grid = Grid(n, m)

def dfs(grid:Grid):
  
